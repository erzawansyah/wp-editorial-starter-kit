# WORDPRESS-SETUP.md — Checklist Setup WordPress

Lakukan semua langkah ini **sebelum** meminta AI memulai Fase Konten atau Fase Tema. WordPress harus sudah bersih, terkonfigurasi, dan terhubung ke WPVibe sebelum AI dilibatkan.

---

## 1. Instalasi WordPress

- [ ] Install WordPress (PHP 8.2+, MySQL 8+ atau MariaDB 10.6+)
- [ ] Atur nama situs, tagline, email admin
- [ ] Set permalink ke **Post name** (`/sample-post/`)
- [ ] Hapus post, page, dan komentar default bawaan WordPress
- [ ] Hapus tema bawaan (Twenty Twenty-*) kecuali satu yang aktif sementara
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
| **WP Recipe Maker** | Niche kuliner — format resep terstruktur |
| **WP-Optimize** | Pembersihan database rutin |
| **UpdraftPlus** | Backup otomatis ke cloud (wajib sebelum deploy ke produksi) |

---

## 4. Setup WPVibe

- [ ] Install plugin WPVibe dari [wpvibe.ai](https://wpvibe.ai)
- [ ] Aktifkan plugin di wp-admin → Plugins
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
- [ ] Thumbnail: 150×150
- [ ] Medium: 300×300
- [ ] Large: 1024×1024

---

## 6. Instalasi Tema _tw

`_tw` adalah base theme yang wajib terinstall di WordPress sebelum AI bisa memulai Fase Tema. AI akan memeriksa keberadaannya via WPVibe — jika belum ada, AI akan memandu proses instalasi.

### Cara Install _tw

**Opsi A — Web Generator (paling mudah):**
1. Buka https://underscoretw.com/
2. Isi nama tema (gunakan slug website, misal `berita-foodies`)
3. Download zip hasil generate
4. Upload ke WordPress: **wp-admin → Appearance → Themes → Add New Theme → Upload Theme**
5. Aktifkan tema tersebut

**Opsi B — WP-CLI (jika tersedia di server):**
```bash
wp package install gregsullivan/wp-cli-tw
wp tw generate --name="Nama Tema" --slug="nama-tema"
wp theme activate nama-tema
```

### Setup Lokal untuk Build Step

Setelah tema terinstall di server, siapkan source _tw di lokal untuk proses build CSS/JS:

```bash
# Di dalam .workspaces/{nama-proyek}/
npx degit gregsullivan/_tw theme-src
cd theme-src
npm install
```

> **Catatan:** Folder `.workspaces/` sudah ada di repo ini dan di-gitignore. Ini tempat yang benar untuk menyimpan source _tw per proyek.

### Verifikasi

- [ ] Tema _tw terinstall di WordPress
- [ ] Tema aktif (Appearance → Themes)
- [ ] Source _tw ada di `.workspaces/{proyek}/theme-src/`
- [ ] `npm install` sudah dijalankan di folder theme-src

---

## 7. Verifikasi Akhir Sebelum Panggil AI

- [ ] WordPress berjalan normal di URL target
- [ ] Permalink sudah di-flush (Settings → Permalinks → Save Changes)
- [ ] WPVibe terkoneksi dan merespons
- [ ] `SITE.md` sudah terisi (URL, nama, niche)
- [ ] `DESIGN.md` sudah terisi (warna, tipografi, layout)
- [ ] Tidak ada error di wp-admin (cek Site Health)
