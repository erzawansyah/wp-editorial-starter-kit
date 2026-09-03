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
| **Yoast SEO** atau **Rank Math** | Meta title, description, sitemap XML, breadcrumb |

### Performa
| Plugin | Keterangan |
|---|---|
| **WP Rocket** atau **LiteSpeed Cache** | Caching, minifikasi CSS/JS |
| **Smush** atau **ShortPixel** | Kompresi gambar otomatis |

### Keamanan
| Plugin | Keterangan |
|---|---|
| **Wordfence** atau **Solid Security** | Firewall, login protection |

### Konten & Editorial
| Plugin | Keterangan |
|---|---|
| **Classic Editor** | Hindari Gutenberg untuk posting editorial standar |
| **Advanced Custom Fields (ACF) Free** | Custom field untuk metadata artikel (penulis, sumber, dsb.) |
| **WPForms Lite** | Form kontak halaman statis |

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

## 6. Tema Sementara

Gunakan tema default WordPress yang paling ringan (misal Twenty Twenty-Four) sebagai placeholder selama fase konten. Tema aktual akan dibangun oleh AI pada Fase Tema dan diaktifkan setelah disetujui.

---

## 7. Verifikasi Akhir Sebelum Panggil AI

- [ ] WordPress berjalan normal di URL target
- [ ] Permalink sudah di-flush (Settings → Permalinks → Save Changes)
- [ ] WPVibe terkoneksi dan merespons
- [ ] `SITE.md` sudah terisi (URL, nama, niche)
- [ ] `DESIGN.md` sudah terisi (warna, tipografi, layout)
- [ ] Tidak ada error di wp-admin (cek Site Health)
