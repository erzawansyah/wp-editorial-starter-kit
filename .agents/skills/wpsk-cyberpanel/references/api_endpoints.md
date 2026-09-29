# CyberPanel API & Internal Route Reference (Agnostic)

Dokumentasi teknis endpoint CyberPanel (OpenLiteSpeed web server) untuk integrasi dan otomatisasi berbasis script.

---

## 1. Mekanisme Autentikasi

CyberPanel memiliki dua jenis layer akses:

### A. Endpoint `/api/*` (Token / Direct JSON Credentials)
Digunakan untuk fungsi dasar seperti pembuatan website. Parameter autentikasi dikirimkan langsung di dalam body JSON:
```json
{
  "adminUser": "<CYBERPANEL_USERNAME>",
  "adminPass": "<CYBERPANEL_PASSWORD>"
}
```
*Catatan:* Parameter `adminUser` dan `adminPass` juga menerima pengguna non-admin (misalnya reseller atau user biasa) asalkan fitur **API Access** telah diaktifkan untuk pengguna tersebut di menu *User > API Access*.

### B. Endpoint `/api/loginAPI` (Session & CSRF Token)
Digunakan untuk mengakses fitur internal seperti File Manager, Database Manager, Penggantian Versi PHP, dan Penerbitan SSL:
- **Metode:** `POST`
- **Content-Type:** `application/x-www-form-urlencoded`
- **Body:** `username=<USER>&password=<PASS>`
- **Hasil:** CyberPanel membuat sesi Django dan mengembalikan cookie `sessionid` dan `csrftoken`.
- **Penggunaan Lanjutan:** Seluruh request berikutnya wajib menyertakan cookie jar tersebut serta header `X-CSRFToken: <csrftoken>`.

---

## 2. Katalog Endpoint Utama

### 1. Pembuatan Website (Virtual Host)
- **Route:** `POST /api/createWebsite`
- **Payload:**
  ```json
  {
    "adminUser": "<CYBERPANEL_USERNAME>",
    "adminPass": "<CYBERPANEL_PASSWORD>",
    "domainName": "<domain>",
    "ownerEmail": "admin@<domain>",
    "packageName": "Default",
    "websiteOwner": "<CYBERPANEL_USERNAME>",
    "ownerPassword": "<CYBERPANEL_PASSWORD>",
    "phpSelection": "PHP 8.3",
    "ssl": 1,
    "dkimCheck": 1,
    "openBasedir": 1
  }
  ```
- **Respons:**
  ```json
  {
    "status": 1,
    "createWebSiteStatus": 1,
    "LinuxUser": "<linux_user>",
    "tempStatusPath": "/home/cyberpanel/<PID>"
  }
  ```

### 2. Manajemen Database MySQL
- **Route Buat DB:** `POST /dataBases/submitDBCreation` (Butuh Session + CSRF)
  ```json
  {
    "databaseWebsite": "<domain>",
    "webUserName": "<truncated_prefix>",
    "dbName": "<suffix>",
    "dbUsername": "<suffix>",
    "dbPassword": "<strong_password>"
  }
  ```
  *Penting:* CyberPanel otomatis menambahkan `<truncated_prefix>_` di depan `dbName` dan `dbUsername`.
- **Route Hapus DB:** `POST /dataBases/submitDatabaseDeletion` (Butuh Session + CSRF)
  ```json
  {
    "dbName": "<full_database_name>"
  }
  ```
- **Route List DB:** `POST /dataBases/fetchDatabases` (Butuh Session + CSRF)
  ```json
  {
    "databaseWebsite": "<domain>"
  }
  ```

### 3. File Manager Controller
- **Route:** `POST /filemanager/controller` (Butuh Session + CSRF)
- **Method `list` (Melihat Berkas):**
  ```json
  {
    "domainName": "<domain>",
    "method": "list",
    "completeStartingPath": "/home/<domain>/public_html"
  }
  ```
- **Method `deleteFolderOrFile` (Hapus Berkas/Folder):**
  ```json
  {
    "domainName": "<domain>",
    "method": "deleteFolderOrFile",
    "path": "/home/<domain>/public_html",
    "fileAndFolders": ["index.html", "temp.zip"],
    "skipTrash": true
  }
  ```
- **Method `extract` (Ekstraksi Arsip):**
  ```json
  {
    "domainName": "<domain>",
    "method": "extract",
    "fileToExtract": "/home/<domain>/public_html/latest.zip",
    "extractionLocation": "/home/<domain>/public_html",
    "extractionType": "zip"
  }
  ```
- **Method `move` (Memindahkan Berkas):**
  ```json
  {
    "domainName": "<domain>",
    "method": "move",
    "basePath": "/home/<domain>/public_html/wordpress",
    "newPath": "/home/<domain>/public_html",
    "fileAndFolders": ["wp-admin", "wp-content", "wp-includes", "index.php", "wp-config-sample.php", "..."]
  }
  ```
- **Method `writeFileContents` (Tulis File Langsung):**
  ```json
  {
    "domainName": "<domain>",
    "method": "writeFileContents",
    "fileName": "/home/<domain>/public_html/wp-config.php",
    "fileContent": "<?php ... ?>"
  }
  ```

### 4. Pengunggahan File Multipart
- **Route:** `POST /filemanager/upload` (Butuh Session + CSRF)
- **Content-Type:** `multipart/form-data`
- **Fields:**
  - `domainName`: `<domain>`
  - `completePath`: `/home/<domain>/public_html`
  - `file`: Stream berkas binary dengan nama berkas asli (misal: `latest.zip`)

### 5. Penyelarasan Versi PHP Website
- **Route:** `POST /websites/changePHP` (Butuh Session + CSRF)
- **Payload:**
  ```json
  {
    "childDomain": "<domain>",
    "phpSelection": "PHP 8.3"
  }
  ```

### 6. Penerbitan Sertifikat SSL (Let's Encrypt / Listener Reload)
- **Route:** `POST /manageSSL/issueSSL` (Butuh Session + CSRF)
- **Payload:**
  ```json
  {
    "virtualHost": "<domain>"
  }
  ```
