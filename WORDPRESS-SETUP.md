# WORDPRESS-SETUP.md - Checklist Setup WordPress

Lakukan semua langkah ini **sebelum** meminta AI memulai Fase Konten atau Fase Tema. WordPress harus sudah bersih, terkonfigurasi, dan terhubung ke WPVibe sebelum AI dilibatkan.

---

## 1. Instalasi WordPress

- [ ] Install WordPress (PHP 8.2+, MySQL 8+ atau MariaDB 10.6+)
- [ ] Atur nama situs, tagline, email admin
- [ ] Set permalink ke **Post name** (`/%postname%/`)
- [ ] Hapus post, page, dan komentar default bawaan WordPress
- [ ] Hapus plugin bawaan yang tidak dipakai (Hello Dolly, Akismet jika tidak digunakan)

---

## 2. Plugin Wajib

Install dan aktifkan semua plugin berikut sebelum memulai:

### SEO
| Plugin | Keterangan |
|---|---|
| **Rank Math** | Meta title, description, sitemap XML, breadcrumb |

### Integrasi AI
| Plugin | Keterangan |
|---|---|
| **WPVibe** | **Wajib.** Koneksi AI agent ke WordPress. Install dari wpvibe.ai |

---

## 3. Plugin Opsional (Sesuai Kebutuhan Niche)

| Plugin | Kapan Dipakai |
|---|---|
| **TablePress** | Jika niche butuh tabel perbandingan (review produk, dsb.) |
| **WP Recipe Maker** | Niche kuliner - format resep terstruktur |
| **WP-Optimize** | Pembersihan database rutin |
| **UpdraftPlus** | Backup otomatis ke cloud (wajib sebelum deploy ke produksi) |

---

## 4. Setup WPVibe

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
- [ ] Format waktu: `H:i`

### Pengaturan Baca
- [ ] Homepage: **Static page** (buat page kosong bernama "Beranda", assign sebagai homepage)
- [ ] Posts page: Buat page kosong "Blog" atau "Artikel", assign sebagai posts page
- [ ] Feed: Tampilkan **ringkasan**, bukan teks penuh

### Pengaturan Diskusi
- [ ] Nonaktifkan komentar secara global jika tidak dibutuhkan
- [ ] Atau aktifkan moderasi komentar jika ingin komentar

### Media
- [ ] Thumbnail: 150x150
- [ ] Medium: 300x300
- [ ] Large: 1024x1024

---

## 6. Base Theme & Starter Code

Karena workflow menggunakan metode "Content Hard-Gate", instalasi awal sangat spesifik:

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

---

## 7. Verifikasi Akhir Sebelum Panggil AI

- [ ] WordPress berjalan normal di URL target
- [ ] WPVibe terkoneksi dan merespons
- [ ] Tema **GeneratePress** sudah aktif
- [ ] Folder `.workspaces/theme-src/` sudah berisi instalasi npm murni
- [ ] Folder `.workspaces/assets/` sudah dibuat
- [ ] `SITE.md` dan `DESIGN.md` sudah terisi (atau panggil `/wpsk-editorial-brainstorm` di chat AI jika butuh ide)

