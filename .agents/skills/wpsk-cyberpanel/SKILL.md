---
name: wpsk-cyberpanel
description: Panduan dan otomatisasi terstandarisasi untuk manajemen dan provisi website, database MySQL, berkas, versi PHP, SSL, serta CMS WordPress di server CyberPanel (OpenLiteSpeed) secara agnostik melalui REST API dan File Manager. Mencakup pembuatan Virtual Host, isolasi database MySQL ({prefix}_wpdb), pengunggahan core CMS/WordPress, penulisan konfigurasi wp-config.php dengan salt resmi, penanganan error 403 MIME handler LSPHP OpenLiteSpeed, sinkronisasi listener SSL, dan inisialisasi instalasi via HTTP. Gunakan skill ini setiap kali diminta berinteraksi dengan CyberPanel, membuat website di CyberPanel, mengelola database/file manager CyberPanel, mengotomatisasi provisi WordPress via API, atau mendiagnosis error 403/404 pada domain CyberPanel.
---

# Manajemen & Provisi Server CyberPanel (Agnostik)

Gunakan skill ini untuk mengotomatisasi seluruh siklus manajemen website, database, berkas, dan CMS berbasis WordPress di server kontrol panel **CyberPanel (OpenLiteSpeed)** tanpa ketergantungan pada IP atau domain tertentu.

> [!CAUTION]
> ### ⚠️ PERINGATAN KEAMANAN MUTLAK: NONAKTIFKAN API ACCESS
> **Fitur API ACCESS di CyberPanel memberikan keleluasaan penuh dan hak kontrol tingkat tinggi** (mencakup pembuatan/penghapusan website, manipulasi database MySQL, hingga akses bebas ke File Manager).
> 
> **PROTOKOL WAJIB AGEN (Sampaikan Selalu Berulang-ulang ke Pengguna):**
> Setiap kali selesai menjalankan operasi, provisi, atau jika pengguna sudah tidak lagi aktif mengelola website bersangkutan, **agen WAJIB selalu mengingatkan pengguna untuk segera MENONAKTIFKAN fitur API ACCESS** pada user CyberPanel terkait (*Users > Modify User > API Access = Disable*) demi menjaga keamanan akun dan integritas server.

---

## 1. Arsitektur & Prinsip Operasi

1. **Akses Dual-Layer CyberPanel:**
   - **Layer API Publik (`/api/*`):** Menggunakan kredensial langsung (`adminUser` & `adminPass`) di dalam payload JSON untuk pembuatan website. Menerima user non-admin selama fitur *API Access* diaktifkan di CyberPanel.
   - **Layer Internal Django (`/api/loginAPI`):** Menghasilkan sesi cookie (`sessionid` & `csrftoken`) untuk berinteraksi dengan File Manager, Database Manager, modul PHP, dan SSL.
2. **Isolasi Penuh (Zero Cross-Contamination):**
   - Setiap website memiliki user Linux tersendiri (misal: `<prefix><angka>`) dan direktori terisolasi di `/home/<domain>/`.
   - Dilarang keras memodifikasi konfigurasi server global di luar parameter vhost yang bersangkutan.
3. **Prefix Database CyberPanel:**
   - CyberPanel membatasi nama database dengan prefix nama domain yang dipotong (maksimal 4 karakter awal jika panjang domain sebelum ekstensi lebih dari 5 karakter). Contoh: domain `example.com` akan menghasilkan prefix `exam_`.
   - Standar nama DB: `<prefix>_wpdb`. Standar user DB: `<prefix>_wpdb`.

---

## 2. Alur Provisi Langkah Demi Langkah

### Langkah 1: Buat Virtual Host / Website
Kirimkan request ke endpoint pembuatan website dengan menyertakan versi PHP yang aktif di server:
- **Endpoint:** `POST /api/createWebsite`
- **Parameter:** `domainName`, `ownerEmail`, `packageName` (default: `Default`), `phpSelection` (sesuaikan dengan binary LSPHP terpasang, misal `PHP 8.3`), `ssl: 1`, `openBasedir: 1`.

### Langkah 2: Buat Database MySQL & User
Masuk melalui sesi `/api/loginAPI` untuk memperoleh CSRF token, kemudian buat database:
- **Endpoint:** `POST /dataBases/submitDBCreation`
- **Parameter:** `databaseWebsite: <domain>`, `webUserName: <prefix>`, `dbName: "wpdb"`, `dbUsername: "wpdb"`, `dbPassword: "<strong_password>"`.

### Langkah 3: Bersihkan Berkas Default
Hapus file landing page bawaan CyberPanel sebelum mengekstrak WordPress:
- **Endpoint:** `POST /filemanager/controller` (Method: `deleteFolderOrFile`)
- **Target:** `/home/<domain>/public_html/index.html`.

### Langkah 4: Unggah & Ekstrak Core WordPress
1. Unduh arsip resmi WordPress terbaru (`https://wordpress.org/latest.zip`).
2. Unggah berkas ke `/home/<domain>/public_html/latest.zip` menggunakan `POST /filemanager/upload` (multipart/form-data).
3. Ekstrak arsip menggunakan `method: "extract"`.
4. Pindahkan seluruh 19 berkas/folder dari `/home/<domain>/public_html/wordpress/*` langsung ke root `/home/<domain>/public_html/` menggunakan `method: "move"`.
5. Hapus file `latest.zip` dan folder `wordpress/` yang sudah kosong.

### Langkah 5: Susun Konfigurasi `wp-config.php`
1. Ambil authentication keys & salts acak resmi langsung dari API: `https://api.wordpress.org/secret-key/1.1/salt/`.
2. Tulis berkas `/home/<domain>/public_html/wp-config.php` via `method: "writeFileContents"` dengan parameter database yang telah dibuat (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST = localhost`).

### Langkah 6: Selaraskan Handler PHP & Muat Ulang Listener
- **Ganti PHP Vhost:** Panggil `POST /websites/changePHP` dengan `childDomain: <domain>` dan `phpSelection: "PHP 8.3"` (atau versi LSPHP yang aktif di OS).
- **Reload Listener (Jika 404):** Panggil `POST /manageSSL/issueSSL` dengan `virtualHost: <domain>` untuk memaksa OpenLiteSpeed memperbarui pemetaan vhost pada listener web server.

### Langkah 7: Inisialisasi CMS WordPress
Kirimkan POST request ke skrip instalasi web WordPress untuk membentuk tabel database dan akun administrator:
- **URL:** `https://<domain>/wp-admin/install.php?step=2`
- **Headers Wajib:** Gunakan browser `User-Agent` standar untuk mencegah blokir WAF/Cloudflare Error 1010.
- **Fields:**
  - `weblog_title`: Judul situs
  - `user_name`: `<domain_name>_admin`
  - `admin_password`: Password kuat acak
  - `admin_email`: Email pengelola (misal: `admin@<domain>`)
  - `blog_public`: `1`
  - `Submit`: `Install WordPress`

### Langkah 8: Konfigurasi Web Server & Easy MCP AI (.htaccess & LiteSpeed Cache)
Agar komunikasi AI client via Model Context Protocol (MCP) tidak terputus:
1. **Aturan `.htaccess` Authorization (Paling Atas):** Letakkan blok ini di baris teratas file `.htaccess` (sebelum `# BEGIN LSCACHE` atau rule dengan flag `[L]`):
   ```apache
   # BEGIN Easy MCP AI
   <IfModule mod_rewrite.c>
   RewriteEngine On
   RewriteCond %{HTTP:Authorization} .
   RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
   </IfModule>
   # END Easy MCP AI
   ```
2. **Pengecualian Cache (LiteSpeed Cache Exclude):**
   - Tambahkan ke *LiteSpeed Cache > Cache > Excludes > Do Not Cache URIs*:
     ```text
     /wp-json/easy-mcp-ai/
     /.well-known/oauth-
     /.well-known/openid-configuration
     ```
   - Matikan opsi **Cache REST API** (*LiteSpeed Cache > Cache > Cache REST API = OFF*).

### Langkah 9: Pengamanan Akun (Peringatan Wajib Nonaktifkan API Access)
Setelah seluruh proses provisi dan verifikasi selesai (atau jika website sudah tidak dikelola lagi):
> [!WARNING]
> **Peringatan Wajib Disampaikan ke Pengguna:**
> *"Seluruh proses provisi dan konfigurasi telah selesai. Jika Anda sudah tidak lagi menggunakan atau mengonfigurasi website ini, **pastikan fitur API ACCESS pada user CyberPanel segera dinonaktifkan** (*Users > Modify User > API Access = Disable*) demi menjaga keamanan akun dan server, karena API Access memberikan keleluasaan akses kontrol penuh."*

---


## 3. Skrip Otomasi Terintegrasi

Skill ini menyediakan utilitas CLI Python yang dapat langsung dieksekusi tanpa konfigurasi manual:

```powershell
# Jalankan provisi penuh WordPress (Website + DB + Core WP + wp-config + Inisialisasi)
python .agents/skills/wpsk-cyberpanel/scripts/cyberpanel_provisioner.py `
  --domain example.com `
  --title "My Example Blog" `
  --admin-user example_admin `
  --admin-email admin@example.com `
  --php "PHP 8.3"
```

Skrip secara otomatis membaca variabel kredensial dari `.env`:
- `CYBERPANEL_URL` (Contoh: `https://panel.domainanda.com:8090/`)
- `CYBERPANEL_USERNAME_1` / `CYBERPANEL_PASSWORD_1` (Akun User 1 untuk website primer)
- `CYBERPANEL_USERNAME_2` / `CYBERPANEL_PASSWORD_2` (Akun User 2 untuk pembagian kuota/resource server)
- Fallback standar: `CYBERPANEL_USERNAME` dan `CYBERPANEL_PASSWORD`

---

## 4. Panduan Troubleshooting Masalah Kritis

| Gejala Error | Akar Masalah | Solusi Teruji |
| :--- | :--- | :--- |
| **403 Forbidden**<br>`MIME type [application/x-httpd-php] for suffix '.php' does not allow serving as static file, access denied!` | OpenLiteSpeed melarang penyajian file PHP sebagai teks statis. Ini terjadi jika versi binary LSPHP (misal `lsphp82` atau `lsphp74`) yang diset pada vhost tidak terpasang di OS server. | Ubah versi PHP vhost ke binary yang aktif di OS (misal `PHP 8.3`) via endpoint `POST /websites/changePHP`. |
| **403 Forbidden (Error Code 1010)** | Cloudflare Browser Integrity Check mendeteksi request otomatis tanpa signature browser. | Tambahkan header browser standar (`User-Agent: Mozilla/5.0 ...`) pada setiap HTTP request ke domain. |
| **404 Not Found pada Domain Baru** | Konfigurasi vhost baru belum dimuat oleh listener OpenLiteSpeed (listener cache). | Panggil endpoint `POST /manageSSL/issueSSL` untuk domain tersebut. Proses sertifikasi SSL otomatis memicu graceful reload pada listener. |
| **404 Not Found pada `/wp-json/`** | WordPress baru belum memiliki konfigurasi rewrite rules `.htaccess` untuk pretty permalinks. | Gunakan endpoint bawaan `https://<domain>/?rest_route=/` untuk verifikasi REST API awal sebelum permalink disimpan di admin panel. |

---

## 5. Referensi Lanjutan

- Untuk detail struktur payload JSON setiap rute API CyberPanel, baca [references/api_endpoints.md](references/api_endpoints.md).
