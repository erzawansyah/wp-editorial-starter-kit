# PROGRESS.md - Tracker Progres Proyek

Salin file ini ke `.workspaces/PROGRESS.md` saat memulai proyek baru.
Update checklist ini secara **real-time** setiap kali satu item selesai dikerjakan.
**File ini adalah sumber kebenaran utama untuk melanjutkan pekerjaan di sesi baru.**

---

**Proyek:** `{{ Nama Website }}`
**URL Target:** `{{ URL WordPress }}`
**Dimulai:** `{{ YYYY-MM-DD }}`
**Target selesai:** `{{ YYYY-MM-DD }}`
**Fase Aktif Saat Ini:** `{{ Setup / Konten / Tema / QA / Deployment }}`
**Fase Aktif Saat Ini:** `{{ Setup / PRD / Tema / Konten / QA / Deployment }}`

---

## Fase 1: Setup (Manusia & Agen)
## Fase 1: Setup & Environment (Manusia & Agen)

- [ ] Clone repo starter kit
- [ ] Buat direktori `.workspaces/assets/`
- [ ] Buat file `.env` dari `.env.example` berisi `WP_USERNAME` dan `WP_APP_PASSWORD`
- [ ] Isi `SITE.md` tanpa placeholder `{{ }}` yang tersisa
- [ ] Isi `DESIGN.md` tanpa placeholder `{{ }}` yang tersisa
- [ ] Selesaikan semua item di `WORDPRESS-SETUP.md`
- [ ] WPVibe terkoneksi dan terverifikasi ke URL di `SITE.md`
- [ ] Tema **GeneratePress** diinstall dan aktif di server target
- [ ] Permalink diubah menjadi `/%postname%/` (hapus `index.php`)
- [ ] Koneksi WP REST API terverifikasi (`GET /wp-json/wp/v2/users/me`)
- [ ] Permalink diatur ke `/%postname%/`
- [ ] Salin file ini ke `.workspaces/PROGRESS.md` dan isi metadata di atas

**✅ FASE 1 SELESAI:** `{{ Tanggal }}`

---

## Fase 2: Konten (@content)
## Fase 2: Perencanaan Arsitektur & PRD (@architect)

### Taksonomi & Navigasi
- [ ] Daftar kategori final disetujui user
- [ ] Kategori dibuat di WordPress (via WPVibe)
- [ ] Tag utama dibuat di WordPress (via WPVibe)
- [ ] Menu navigasi utama disusun dan diregistrasi
- [ ] Analisis niche dan persyaratan desain dari `SITE.md` & `DESIGN.md`
- [ ] Buat dokumen PRD di `PRODUCT.md` (pastikan masuk `.gitignore`)
- [ ] Definisikan daftar seluruh template (`front-page.php`, `single.php`, `page.php`, `archive.php`, `search.php`, `404.php`, template-parts)
- [ ] Susun struktur wireframe detail untuk **Frontpage** (Hero grid, Section kategori, Trending, Sidebar)
- [ ] Susun struktur wireframe detail untuk **Single Article** (Post header, Author bio, Breadcrumb, Gutenberg layout, Related posts, Comment)

### Halaman Statis (via WPVibe, format Gutenberg Blocks)
- [ ] Tentang Kami
- [ ] Tim Redaksi
- [ ] Kebijakan Privasi
- [ ] Syarat & Ketentuan
- [ ] Kontak
- [ ] `{{ Halaman statis lain sesuai niche }}`

### Aset Visual
- [ ] Logo (format SVG + PNG, diunggah ke Media Library)
- [ ] Favicon (format ICO + PNG 192px)
- [ ] OG image default (1200x630px)
- [ ] Semua aset di atas disimpan di `.workspaces/assets/` sebelum diunggah

### Konten Artikel (via WPVibe, format Gutenberg Blocks + Featured Image)
- [ ] Minimal 3 artikel SEO per kategori utama diinjeksi via DB
- [ ] Setiap artikel memiliki Featured Image yang sudah di-set

---

> ## ⛔ HARD GATE: VALIDASI KONTEN OLEH USER
> ## ⛔ HARD GATE: VALIDASI PRD OLEH USER
>
> Agen **WAJIB BERHENTI** di sini dan meminta user melakukan visual review di browser menggunakan tema GeneratePress yang aktif. Fase Tema **tidak boleh dimulai** sebelum baris di bawah ini terisi.
> Agen **WAJIB BERHENTI** di sini dan meminta user meninjau dokumen `PRODUCT.md`. Fase Tema **tidak boleh dimulai** sebelum baris di bawah ini terisi dan disetujui.
>
> **Status:** `[ ] MENUNGGU PERSETUJUAN` → `[ ] DISETUJUI oleh user pada {{ Tanggal }}`
>
> **Catatan review user:** `{{ Catat catatan atau koreksi dari user di sini }}`
> **Catatan review user:** `{{ Catat masukan atau revisi wireframe dari user di sini }}`

---

**✅ FASE 2 SELESAI & HARD GATE DILEWATI:** `{{ Tanggal }}`

---

## Fase 3: Tema (@architect → @engineer)
## Fase 3: Pengembangan Tema (@engineer)

> **FASE INI TIDAK BOLEH DIMULAI** sebelum baris "HARD GATE DILEWATI" di atas terisi.
> **FASE INI TIDAK BOLEH DIMULAI** sebelum baris "HARD GATE PRD DILEWATI" di atas terisi.

### Prasyarat Teknis
- [ ] Skill `wpsk-theme-convention/SKILL.md` sudah dibaca penuh
- [ ] Skill `antislop-ui/SKILL.md` sudah dibaca
- [ ] Skill `antislop-human/SKILL.md` sudah dibaca
- [ ] Skill `antislop-layoutmobile/SKILL.md` sudah dibaca
- [ ] Skill `frontend-design/SKILL.md` sudah dibaca
- [ ] Dokumen `PRODUCT.md` dan `DESIGN.md` sudah dipelajari
- [ ] Theme source di-scaffold di `.workspaces/theme-src/` dari underscoretw.com
- [ ] `npm install` berhasil dijalankan
- [ ] `npm run dev` berhasil — `theme/style.css` ter-generate

### Konfigurasi Tema
### Konfigurasi & Fungsi Tema
- [ ] Nama tema di `theme/style.css` diubah dari `_tw` ke nama situs dari `SITE.md`
- [ ] `functions.php` mendeklarasikan `add_theme_support('custom-logo')`
- [ ] `functions.php` mendeklarasikan `register_nav_menus()` dengan lokasi yang sesuai
- [ ] `functions.php` mendeklarasikan `add_theme_support('post-thumbnails')`
- [ ] Warna dan font di `tailwind.css` diambil dari `DESIGN.md` (tidak ada nilai inventif)
- [ ] Token warna dan tipografi di `tailwind.css` diambil dari `DESIGN.md`

### Template Parts
### Template Parts & File Template (Mengacu ke `PRODUCT.md`)
- [ ] `template-parts/content/content-card.php`
- [ ] `template-parts/content/content-single.php`
- [ ] `template-parts/content/content-none.php`
- [ ] `template-parts/homepage/hero-grid.php`
- [ ] `template-parts/homepage/section-category.php`
- [ ] `template-parts/homepage/section-trending.php`
- [ ] `template-parts/post/post-meta.php`
- [ ] `template-parts/post/post-thumbnail.php`

### File Template Utama
- [ ] `front-page.php` (homepage dengan hero + section kategori + trending)
- [ ] `front-page.php` (sesuai wireframe `PRODUCT.md`)
- [ ] `header.php` (logo via `the_custom_logo()`, nav via `wp_nav_menu()`)
- [ ] `footer.php`
- [ ] `single.php` (single post)
- [ ] `single.php` (sesuai wireframe `PRODUCT.md`)
- [ ] `page.php` (single page statis)
- [ ] `archive.php` (archive kategori)
- [ ] `search.php`
- [ ] `404.php`

### Verifikasi Elemen Dinamis (Critical)
### Verifikasi Elemen Dinamis & Anti-Slop
- [ ] **Tidak ada** hardcode HTML navigasi — semua `wp_nav_menu()`
- [ ] **Tidak ada** hardcode `<img>` untuk logo — semua `the_custom_logo()`
- [ ] **Tidak ada** hardcode ID/slug artikel — semua `WP_Query`
- [ ] **Tidak ada** Tailwind CDN di `header.php` atau `functions.php`
- [ ] Semua output PHP di-escape (`esc_html()`, `esc_url()`, `wp_kses_post()`)
- [ ] Kontras warna teks memenuhi WCAG (min 4.5:1 untuk body text)
- [ ] Layout mobile (375px) bebas horizontal scroll dan tap target >= 44px

### Checklist Anti-Slop UI
- [ ] Palet warna berasal dari `DESIGN.md`, bukan default AI
- [ ] Tidak ada gradien biru-ungu generik tanpa justifikasi di `DESIGN.md`
- [ ] Layout mobile (375px) sudah diuji secara terpisah
- [ ] Kontras warna teks sudah diverifikasi (min 4.5:1 untuk body text)
- [ ] Tidak ada elemen dinamis/animasi yang berjalan tanpa trigger user

### Finalisasi
### Finalisasi & Serah Terima Tema
- [ ] Screenshot 1200x900px homepage disimpan sebagai `theme/screenshot.png`
- [ ] `npm run bundle` berhasil dijalankan
- [ ] File `.zip` ada di root `.workspaces/` (bukan di dalam `theme-src/`)
- [ ] File `.zip` **tidak ada** di dalam `theme-src/`
- [ ] `.workspaces/THEME_SPECS.md` sudah digenerate
- [ ] File `.zip` berada di root `.workspaces/` (bukan di dalam `theme-src/`)
- [ ] File `.zip` diserahkan kepada user untuk diunggah/diaktifkan
- [ ] Dokumen `.workspaces/THEME_SPECS.md` digenerate

**✅ FASE 3 SELESAI:** `{{ Tanggal }}`

---

## Fase 4: QA (@qa)
## Fase 4: Manajemen Penulis & Konten (@content)

### Pembuatan User Author via WP REST API
- [ ] 3–5 akun user dengan role `author` berhasil dibuat via REST API
- [ ] Format email diverifikasi: `<username>@<site.com>` untuk setiap author
- [ ] Daftar ID author dicatat untuk rotasi penulisan artikel

### Taksonomi & Halaman Statis via WP REST API
- [ ] Kategori dibuat via REST API (`POST /wp-json/wp/v2/categories`)
- [ ] Tag utama dibuat via REST API (`POST /wp-json/wp/v2/tags`)
- [ ] Menu navigasi disusun dan dikaitkan
- [ ] Halaman statis format Gutenberg dibuat via REST API (Tentang Kami, Tim Redaksi, Kontak, Privasi, Syarat & Ketentuan)

### Aset Visual
- [ ] Logo situs (SVG & PNG) diunggah ke Media Library
- [ ] Favicon (ICO & PNG 192px)
- [ ] OG Image default (1200x630px)
- [ ] Seluruh aset tersimpan rapi di `.workspaces/assets/`

### Penulisan Artikel Paralel via Subagents
- [ ] Pemanggilan subagents secara paralel untuk menulis draf artikel SEO
- [ ] Setiap artikel memenuhi standar skill `seo-article`
- [ ] Setiap artikel menggunakan sintaks Gutenberg Blocks murni (`wp-patterns`)
- [ ] Featured Image dicari (dapat menggunakan WPVibe `search_images`) dan di-set sebagai post thumbnail
- [ ] Setiap artikel dipublikasikan via REST API diatribusikan ke author bergantian (**bukan admin**)
- [ ] Minimal 3 artikel per kategori utama berhasil terbit

**✅ FASE 4 SELESAI:** `{{ Tanggal }}`

---

## Fase 5: QA (@qa)

- [ ] Lighthouse Performa >= 80
- [ ] Lighthouse SEO >= 80
- [ ] Lighthouse Aksesibilitas >= 80
- [ ] Tidak ada broken link di navigasi dan footer
- [ ] Tampilan mobile (375px) — tidak ada horizontal scroll, tap target >= 44px
- [ ] Tampilan tablet (768px)
- [ ] Tampilan desktop (1280px)
- [ ] Sitemap XML tersedia dan dapat diakses
- [ ] Tidak ada broken link di navigasi, konten, dan footer
- [ ] Uji responsivitas mobile (375px) — tap target >= 44px, no overflow
- [ ] Uji responsivitas tablet (768px)
- [ ] Uji responsivitas desktop (1280px)
- [ ] XML Sitemap dapat diakses dan valid

**✅ FASE 4 SELESAI:** `{{ Tanggal }}`
**✅ FASE 5 SELESAI:** `{{ Tanggal }}`

---

## Fase 5: Deployment (Manusia)
## Fase 6: Deployment & Serah Terima (Manusia)

- [ ] File tema `.zip` terbaru dari `.workspaces/` aktif di WordPress
- [ ] Backup pre-deploy tersimpan
- [ ] File tema `.zip` di-upload manual ke `wp-admin → Appearance → Themes → Upload`
- [ ] Tema diaktifkan dan site diperiksa secara visual
- [ ] Post-launch check: homepage, artikel contoh, halaman statis, sitemap
- [ ] Validasi visual langsung di browser bersama konten live
- [ ] Post-launch check: homepage, single article, halaman statis, search, 404

**✅ PROYEK SELESAI:** `{{ Tanggal }}`

---

## Catatan Proyek

`{{ Catat hambatan, keputusan desain, atau perubahan dari rencana awal di sini }}`
