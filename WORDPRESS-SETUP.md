# WORDPRESS-SETUP.md - Checklist Setup WordPress

Lakukan semua langkah ini **sebelum** meminta AI memulai Fase Konten atau Fase Tema. WordPress harus sudah bersih, terkonfigurasi, dan terhubung ke WPVibe sebelum AI dilibatkan.
Lakukan semua langkah ini **sebelum** meminta AI memulai alur kerja utama. WordPress harus sudah bersih, terkonfigurasi, dan kredensial REST API siap digunakan oleh AI.

---

## 1. Instalasi WordPress

- [ ] Install WordPress (PHP 8.2+, MySQL 8+ atau MariaDB 10.6+)
- [ ] Atur nama situs, tagline, email admin
- [ ] Set permalink ke **Post name** (`/%postname%/`)
- [ ] Hapus post, page, dan komentar default bawaan WordPress
- [ ] Hapus plugin bawaan yang tidak dipakai (Hello Dolly, Akismet jika tidak digunakan)

---

## 2. Plugin Wajib
## 2. Kredensial & Integrasi AI

Install dan aktifkan semua plugin berikut sebelum memulai:
Agen AI mengelola konten (pembuatan author, taksonomi, halaman statis, dan artikel) melalui **WordPress REST API** resmi dengan Application Password.

### SEO
| Plugin | Keterangan |
|---|---|
| **Rank Math** | Meta title, description, sitemap XML, breadcrumb |
### A. Buat Application Password (Wajib)
1. Masuk ke dashboard WordPress: `wp-admin → Users → Profile` (atau edit profil admin Anda).
2. Scroll ke bawah ke bagian **Application Passwords**.
3. Masukkan nama aplikasi (misal: `Antigravity Agent`), lalu klik **Add New Application Password**.
4. Salin password yang dihasilkan (format: `xxxx xxxx xxxx xxxx xxxx`).

### Integrasi AI
### B. Konfigurasi File `.env` (Wajib)
Buat file `.env` di root direktori repo ini dengan menyalin `.env.example`:
```env
WP_USERNAME=username_admin_anda
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx
```
*(Catatan: File `.env` sudah masuk dalam `.gitignore` sehingga kredensial aman).*

### C. Plugin WPVibe (Opsional / Pelengkap)
| Plugin | Keterangan |
|---|---|
| **WPVibe** | **Wajib.** Koneksi AI agent ke WordPress. Install dari wpvibe.ai |
| **WPVibe** | Opsional. Digunakan AI untuk operasi di luar REST API standar, seperti pencarian referensi gambar (`search_images`). Install dari wpvibe.ai jika dibutuhkan. |

---

## 3. Plugin Opsional (Sesuai Kebutuhan Niche)
## 3. Plugin Pendukung SEO & Konten

| Plugin | Kapan Dipakai |
Install dan aktifkan plugin pendukung sebelum memulai:

| Plugin | Keterangan |
|---|---|
| **TablePress** | Jika niche butuh tabel perbandingan (review produk, dsb.) |
| **WP Recipe Maker** | Niche kuliner - format resep terstruktur |
| **WP-Optimize** | Pembersihan database rutin |
| **UpdraftPlus** | Backup otomatis ke cloud (wajib sebelum deploy ke produksi) |
| **Rank Math** | Meta title, description, sitemap XML, schema, breadcrumbs |
| **TablePress** | *(Opsional)* Jika niche butuh tabel perbandingan/data terstruktur |
| **WP-Optimize** | Pembersihan cache & optimasi database |
| **UpdraftPlus** | Backup rutin ke cloud |

---

## 4. Setup WPVibe
## 4. Konfigurasi Dasar WordPress

- [ ] Install plugin WPVibe dari [wpvibe.ai](https://wpvibe.ai)
- [ ] Aktifkan plugin di wp-admin -> Plugins
- [ ] Ikuti proses koneksi di dashboard WPVibe (generate & paste API key)
- [ ] Catat URL situs dan masukkan ke `SITE.md` field **URL**
- [ ] Verifikasi koneksi: AI agent harus bisa merespons query WPVibe ke URL tersebut

---

## 5. Konfigurasi Dasar WordPress

### Pengaturan Umum
- [ ] Timezone sesuai lokasi target pembaca (umumnya `Asia/Jakarta`)
- [ ] Format tanggal: `d F Y` (contoh: 3 September 2026)
- [ ] Format tanggal: `d F Y` (contoh: 10 September 2026)
- [ ] Format waktu: `H:i`

### Pengaturan Baca
- [ ] Homepage: **Static page** (buat page kosong bernama "Beranda", assign sebagai homepage)
- [ ] Posts page: Buat page kosong "Blog" atau "Artikel", assign sebagai posts page
- [ ] Feed: Tampilkan **ringkasan**, bukan teks penuh

### Pengaturan Diskusi
- [ ] Nonaktifkan komentar secara global jika tidak dibutuhkan
- [ ] Atau aktifkan moderasi komentar jika ingin komentar
### Pengaturan Diskusi & Media
- [ ] Nonaktifkan komentar jika situs murni editorial tanpa interaksi pembaca
- [ ] Ukuran Media: Thumbnail (150x150), Medium (300x300), Large (1024x1024)

### Media
- [ ] Thumbnail: 150x150
- [ ] Medium: 300x300
- [ ] Large: 1024x1024

---

## 6. Base Theme & Starter Code
## 5. Source Code Tema Lokal (_tw)

Karena workflow menggunakan metode "Content Hard-Gate", instalasi awal sangat spesifik:
Siapkan _source code_ `_tw` murni di direktori `.workspaces/` agar AI dapat mem-build tema kustom pada Fase Tema:

### A. Tema Aktif (WordPress Server)
- [ ] Pastikan **GeneratePress** (atau tema netral lain) adalah tema yang saat ini **AKTIF** di WordPress server.
- [ ] Ini penting agar Manusia bisa memvalidasi kesiapan konten sebelum AI membangun tema kustom.

### B. Source Code Tema Lokal (_tw)
Siapkan _source code_ `_tw` murni di direktori `.workspaces/` agar AI memiliki bahan baku untuk di-*build* pada Fase Tema nanti.

```bash
# Di root repo starter kit:
cd .workspaces
npx degit gregsullivan/_tw theme-src
cd theme-src
npm install
```

> **Catatan:** AI akan secara otomatis me-rename identitas tema dari `_tw` menjadi nama situs Anda pada saat Fase Tema dimulai.
> **Catatan:** AI akan secara otomatis menyesuaikan identitas tema dari `_tw` menjadi nama situs Anda mengacu pada `SITE.md` dan spesifikasi `PRODUCT.md`.

---

## 7. Verifikasi Akhir Sebelum Panggil AI
## 6. Verifikasi Akhir Sebelum Panggil AI

- [ ] WordPress berjalan normal di URL target
- [ ] WPVibe terkoneksi dan merespons
- [ ] Tema **GeneratePress** sudah aktif
- [ ] Folder `.workspaces/theme-src/` sudah berisi instalasi npm murni
- [ ] WordPress berjalan normal di URL target (tercatat di `SITE.md`)
- [ ] File `.env` terisi dengan `WP_USERNAME` dan `WP_APP_PASSWORD` role admin yang valid
- [ ] Folder `.workspaces/theme-src/` sudah terinstal `npm install`
- [ ] Folder `.workspaces/assets/` sudah dibuat
- [ ] `SITE.md` dan `DESIGN.md` sudah terisi (atau panggil `/wpsk-editorial-brainstorm` di chat AI jika butuh ide)

- [ ] `SITE.md` dan `DESIGN.md` sudah terisi (atau panggil `/wpsk-editorial-brainstorm` di chat AI jika butuh panduan ide)
