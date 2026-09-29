#!/usr/bin/env python3
"""
cyberpanel_provisioner.py
Skrip otomatisasi agnostik untuk provisi website, database, berkas core WordPress,
dan inisialisasi CMS di server CyberPanel (OpenLiteSpeed).

Bebas dari hardcoded IP dan domain spesifik.
Membaca kredensial dari .env atau argumen baris perintah.
"""

import os
import sys
import time
import json
import ssl
import secrets
import string
import argparse
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar

def load_env():
    env = {}
    search_paths = [
        '.env',
        os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '.env'),
        os.path.join(os.getcwd(), '.env')
    ]
    for p in search_paths:
        if os.path.isfile(p):
            with open(p, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and '=' in line and not line.startswith('#'):
                        k, v = line.split('=', 1)
                        env[k.strip()] = v.strip().strip('\'"')
            break
    return env

def generate_strong_password(length=20):
    chars = string.ascii_letters + string.digits + "!@#%^&*"
    return ''.join(secrets.choice(chars) for _ in range(length))

def get_truncated_web_name(domain: str) -> str:
    """Mengikuti logika truncating nama CyberPanel: maks 4 karakter pertama jika > 5 char."""
    clean = domain.replace('-', '').split('.')[0]
    return clean[:4] if len(clean) > 5 else clean

def fetch_wordpress_salts():
    """Mengambil authentication keys & salts resmi dari API WordPress.org."""
    try:
        with urllib.request.urlopen('https://api.wordpress.org/secret-key/1.1/salt/', timeout=10) as r:
            return r.read().decode('utf-8')
    except Exception:
        # Fallback jika offline
        keys = ['AUTH_KEY', 'SECURE_AUTH_KEY', 'LOGGED_IN_KEY', 'NONCE_KEY',
                'AUTH_SALT', 'SECURE_AUTH_SALT', 'LOGGED_IN_SALT', 'NONCE_SALT']
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_"
        return '\n'.join([f"define('{k}', '{''.join(secrets.choice(chars) for _ in range(64))}');" for k in keys]) + '\n'

class CyberPanelClient:
    def __init__(self, base_url=None, username=None, password=None):
        env = load_env()
        self.base_url = (base_url or env.get('CYBERPANEL_URL', '')).rstrip('/')
        self.user = username or env.get('CYBERPANEL_USERNAME', '')
        self.password = password or env.get('CYBERPANEL_PASSWORD', '')

        if not self.base_url or not self.user or not self.password:
            raise ValueError("Kredensial CyberPanel belum diatur. Atur CYBERPANEL_URL, CYBERPANEL_USERNAME, dan CYBERPANEL_PASSWORD di .env atau via argumen.")

        self.cj = http.cookiejar.CookieJar()
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.cj),
            urllib.request.HTTPSHandler(context=self.ctx)
        )
        self.csrf = None
        self._login()

    def _login(self):
        login_data = urllib.parse.urlencode({'username': self.user, 'password': self.password}).encode('utf-8')
        req = urllib.request.Request(
            f"{self.base_url}/api/loginAPI",
            data=login_data,
            headers={'User-Agent': 'CyberPanelProvisioner/1.0'}
        )
        self.opener.open(req)
        for c in self.cj:
            if c.name == 'csrftoken':
                self.csrf = c.value
                break
        if not self.csrf:
            raise RuntimeError("Gagal mendapatkan CSRF token dari CyberPanel loginAPI.")

    def create_website(self, domain, php_version="PHP 8.3", package="Default", email=None):
        payload = {
            "adminUser": self.user,
            "adminPass": self.password,
            "domainName": domain,
            "ownerEmail": email or f"admin@{domain}",
            "packageName": package,
            "websiteOwner": self.user,
            "ownerPassword": self.password,
            "phpSelection": php_version,
            "ssl": 1,
            "dkimCheck": 1,
            "openBasedir": 1
        }
        url = f"{self.base_url}/api/createWebsite"
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json', 'User-Agent': 'CyberPanelProvisioner/1.0'},
            method='POST'
        )
        with self.opener.open(req, timeout=45) as resp:
            return json.loads(resp.read().decode('utf-8'))

    def create_database(self, domain, db_suffix="wpdb", user_suffix="wpdb", db_pass=None):
        prefix = get_truncated_web_name(domain)
        password = db_pass or generate_strong_password()
        payload = {
            'webUserName': prefix,
            'databaseWebsite': domain,
            'dbName': db_suffix,
            'dbUsername': user_suffix,
            'dbPassword': password
        }
        req = urllib.request.Request(
            f"{self.base_url}/dataBases/submitDBCreation",
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'X-CSRFToken': self.csrf,
                'Referer': f"{self.base_url}/dataBases/createDatabase"
            }
        )
        with self.opener.open(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            data['db_password'] = password
            data['full_db_name'] = f"{prefix}_{db_suffix}"
            data['full_db_user'] = f"{prefix}_{user_suffix}"
            return data

    def fm_controller(self, domain, method, extra_payload):
        payload = {'domainName': domain, 'method': method}
        payload.update(extra_payload)
        req = urllib.request.Request(
            f"{self.base_url}/filemanager/controller",
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'X-CSRFToken': self.csrf,
                'Referer': f"{self.base_url}/filemanager/{domain}"
            }
        )
        with self.opener.open(req, timeout=60) as resp:
            return json.loads(resp.read().decode('utf-8'))

    def upload_archive(self, domain, target_folder, local_file_path):
        filename = os.path.basename(local_file_path)
        boundary = "----WebKitFormBoundary" + os.urandom(16).hex()
        parts = [
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"domainName\"\r\n\r\n{domain}\r\n".encode(),
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"completePath\"\r\n\r\n{target_folder}\r\n".encode(),
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\nContent-Type: application/zip\r\n\r\n".encode()
        ]
        with open(local_file_path, 'rb') as f:
            parts.append(f.read())
        parts.append(f"\r\n--{boundary}--\r\n".encode())
        body = b''.join(parts)

        req = urllib.request.Request(
            f"{self.base_url}/filemanager/upload",
            data=body,
            headers={
                'Content-Type': f'multipart/form-data; boundary={boundary}',
                'Content-Length': str(len(body)),
                'X-CSRFToken': self.csrf,
                'Referer': f"{self.base_url}/filemanager/{domain}"
            }
        )
        with self.opener.open(req, timeout=180) as resp:
            return json.loads(resp.read().decode('utf-8'))

    def change_php(self, domain, php_version="PHP 8.3"):
        payload = {'childDomain': domain, 'phpSelection': php_version}
        req = urllib.request.Request(
            f"{self.base_url}/websites/changePHP",
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'X-CSRFToken': self.csrf,
                'Referer': f"{self.base_url}/websites/{domain}"
            }
        )
        with self.opener.open(req, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))

    def issue_ssl(self, domain):
        payload = {'virtualHost': domain}
        req = urllib.request.Request(
            f"{self.base_url}/manageSSL/issueSSL",
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'X-CSRFToken': self.csrf,
                'Referer': f"{self.base_url}/manageSSL/"
            }
        )
        with self.opener.open(req, timeout=90) as resp:
            return json.loads(resp.read().decode('utf-8'))

def provision_full_wordpress(client: CyberPanelClient, domain: str, title: str, admin_user: str, admin_email: str, php_version="PHP 8.3", zip_path=None):
    print(f"[*] Memulai provisi otomatis untuk domain: {domain}")

    # 1. Pembuatan Website
    print(f"  [1/6] Membuat Virtual Host...")
    site_res = client.create_website(domain, php_version=php_version)
    if site_res.get('status') != 1 and site_res.get('createWebSiteStatus') != 1:
        print(f"  [!] Perhatian: {site_res.get('error_message')}")
    time.sleep(5)

    # 2. Pembuatan Database
    print(f"  [2/6] Membuat Database MySQL...")
    db_res = client.create_database(domain, db_suffix="wpdb", user_suffix="wpdb")
    db_name = db_res['full_db_name']
    db_user = db_res['full_db_user']
    db_pass = db_res['db_password']
    print(f"        DB: {db_name} | User: {db_user}")

    public_html = f"/home/{domain}/public_html"

    # 3. Hapus index.html default
    print(f"  [3/6] Membersihkan index.html default...")
    client.fm_controller(domain, 'deleteFolderOrFile', {
        'path': public_html,
        'fileAndFolders': ['index.html'],
        'skipTrash': True
    })

    # 4. Unggah & Ekstrak WordPress
    print(f"  [4/6] Mengunggah paket WordPress...")
    if not zip_path or not os.path.isfile(zip_path):
        temp_zip = os.path.join(os.getcwd(), 'latest.zip')
        if not os.path.isfile(temp_zip):
            print("        Mengunduh latest.zip dari wordpress.org...")
            urllib.request.urlretrieve('https://wordpress.org/latest.zip', temp_zip)
        zip_path = temp_zip

    client.upload_archive(domain, public_html, zip_path)
    client.fm_controller(domain, 'extract', {
        'fileToExtract': f"{public_html}/{os.path.basename(zip_path)}",
        'extractionLocation': public_html,
        'extractionType': 'zip'
    })
    time.sleep(4)

    # Pindahkan berkas dari folder wordpress/ ke public_html/
    wp_dir = f"{public_html}/wordpress"
    items = client.fm_controller(domain, 'list', {'completeStartingPath': wp_dir})
    files_to_move = [v[0] for k, v in items.items() if k not in ['status', 'error_message'] and isinstance(v, list)]
    if files_to_move:
        client.fm_controller(domain, 'move', {
            'basePath': wp_dir,
            'newPath': public_html,
            'fileAndFolders': files_to_move
        })

    client.fm_controller(domain, 'deleteFolderOrFile', {
        'path': public_html,
        'fileAndFolders': [os.path.basename(zip_path), 'wordpress'],
        'skipTrash': True
    })

    # 5. Tulis wp-config.php
    print(f"  [5/6] Menyusun konfigurasi wp-config.php...")
    salts = fetch_wordpress_salts()
    wp_config = f"""<?php
define('DB_NAME', '{db_name}');
define('DB_USER', '{db_user}');
define('DB_PASSWORD', '{db_pass}');
define('DB_HOST', 'localhost');
define('DB_CHARSET', 'utf8mb4');
define('DB_COLLATE', '');

{salts}

$table_prefix = 'wp_';
define('WP_DEBUG', false);

if (!defined('ABSPATH')) {{
    define('ABSPATH', __DIR__ . '/');
}}
require_once ABSPATH . 'wp-settings.php';
"""
    client.fm_controller(domain, 'writeFileContents', {
        'fileName': f"{public_html}/wp-config.php",
        'fileContent': wp_config
    })

    # Selaraskan PHP version & terbitkan SSL untuk me-reload OpenLiteSpeed
    client.change_php(domain, php_version)
    time.sleep(3)

    # 6. Inisialisasi CMS WordPress via HTTP
    print(f"  [6/6] Menginisialisasi instalasi WordPress...")
    admin_pass = generate_strong_password()
    ctx = ssl.create_default_context()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Referer': f"https://{domain}/wp-admin/install.php?step=1",
        'Origin': f"https://{domain}"
    }
    post_data = urllib.parse.urlencode({
        'weblog_title': title,
        'user_name': admin_user,
        'admin_password': admin_pass,
        'admin_password2': admin_pass,
        'pw_weak': 'on',
        'admin_email': admin_email,
        'blog_public': '1',
        'language': '',
        'Submit': 'Install WordPress'
    }).encode('utf-8')

    req = urllib.request.Request(f"https://{domain}/wp-admin/install.php?step=2", data=post_data, headers=headers)
    success = False
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                if 'Success!' in content or 'Berhasil!' in content or 'step=login' in content:
                    success = True
                    break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # Listener reload fallback: terbitkan SSL
                print("        Memicu reload SSL listener...")
                client.issue_ssl(domain)
            time.sleep(4)

    return {
        "domain": domain,
        "success": success,
        "site_title": title,
        "db_name": db_name,
        "db_user": db_user,
        "db_pass": db_pass,
        "admin_user": admin_user,
        "admin_pass": admin_pass,
        "admin_email": admin_email,
        "login_url": f"https://{domain}/wp-login.php"
    }

def main():
    parser = argparse.ArgumentParser(description="Agnostic CyberPanel WordPress Provisioner")
    parser.add_argument("--domain", required=True, help="Nama domain (e.g. example.com)")
    parser.add_argument("--title", default="", help="Judul situs WordPress")
    parser.add_argument("--admin-user", default="", help="Username admin WordPress")
    parser.add_argument("--admin-email", default="", help="Email admin WordPress")
    parser.add_argument("--php", default="PHP 8.3", help="Versi PHP (default: 'PHP 8.3')")
    parser.add_argument("--zip", default="", help="Path berkas latest.zip lokal (opsional)")

    args = parser.parse_args()

    domain = args.domain.strip()
    clean_name = domain.split('.')[0].replace('-', '_')
    title = args.title.strip() or clean_name.capitalize()
    admin_user = args.admin_user.strip() or f"{clean_name}_admin"
    admin_email = args.admin_email.strip() or f"admin@{domain}"

    client = CyberPanelClient()
    res = provision_full_wordpress(
        client=client,
        domain=domain,
        title=title,
        admin_user=admin_user,
        admin_email=admin_email,
        php_version=args.php,
        zip_path=args.zip
    )

    print("\n" + "="*50)
    print("HASIL PROVISI WORDPRESS CYBERPANEL")
    print("="*50)
    print(json.dumps(res, indent=2))
    print("\n" + "!" * 65)
    print(" ⚠️  PERINGATAN KEAMANAN PENTING:")
    print(" Jika website ini sudah tidak lagi memerlukan konfigurasi otomatis,")
    print(" PASTIKAN fitur API ACCESS pada user CyberPanel segera DINONAKTIFKAN.")
    print(" (CyberPanel Admin > Users > Modify User > API Access = Disable)")
    print(" API ACCESS memberikan keleluasaan akses kontrol penuh ke server.")
    print("!" * 65 + "\n")

if __name__ == '__main__':
    main()

