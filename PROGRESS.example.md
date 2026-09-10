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

---

## Fase 1: Setup (Manusia & Agen)

- [ ] Clone repo starter kit
- [ ] Buat direktori `.workspaces/assets/`
- [ ] Isi `SITE.md` tanpa placeholder `{{ }}` yang tersisa
- [ ] Isi `DESIGN.md` tanpa placeholder `{{ }}` yang tersisa
- [ ] Selesaikan semua item di `WORDPRESS-SETUP.md`
- [ ] WPVibe terkoneksi dan terverifikasi ke URL di `SITE.md`
- [ ] Tema **GeneratePress** diinstall dan aktif di server target
- [ ] Permalink diubah menjadi `/%postname%/` (hapus `index.php`)
- [ ] Salin file ini ke `.workspaces/PROGRESS.md` dan isi metadata di atas

**✅ FASE 1 SELESAI:** `{{ Tanggal }}`

---

## Fase 2: Konten (@content)

### Taksonomi & Navigasi
- [ ] Daftar kategori final disetujui user
- [ ] Kategori dibuat di WordPress (via WPVibe)
- [ ] Tag utama dibuat di WordPress (via WPVibe)
- [ ] Menu navigasi utama disusun dan diregistrasi

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
>
> Agen **WAJIB BERHENTI** di sini dan meminta user melakukan visual review di browser menggunakan tema GeneratePress yang aktif. Fase Tema **tidak boleh dimulai** sebelum baris di bawah ini terisi.
>
> **Status:** `[ ] MENUNGGU PERSETUJUAN` → `[ ] DISETUJUI oleh user pada {{ Tanggal }}`
>
> **Catatan review user:** `{{ Catat catatan atau koreksi dari user di sini }}`

---

**✅ FASE 2 SELESAI & HARD GATE DILEWATI:** `{{ Tanggal }}`

---

## Fase 3: Tema (@architect → @engineer)

> **FASE INI TIDAK BOLEH DIMULAI** sebelum baris "HARD GATE DILEWATI" di atas terisi.

### Prasyarat Teknis
- [ ] Skill `wpsk-theme-convention/SKILL.md` sudah dibaca penuh
- [ ] Skill `antislop-ui/SKILL.md` sudah dibaca
- [ ] Skill `antislop-human/SKILL.md` sudah dibaca
- [ ] Skill `antislop-layoutmobile/SKILL.md` sudah dibaca
- [ ] Skill `frontend-design/SKILL.md` sudah dibaca
- [ ] Theme source di-scaffold di `.workspaces/theme-src/` dari underscoretw.com
- [ ] `npm install` berhasil dijalankan
- [ ] `npm run dev` berhasil — `theme/style.css` ter-generate

### Konfigurasi Tema
- [ ] Nama tema di `theme/style.css` diubah dari `_tw` ke nama situs dari `SITE.md`
- [ ] `functions.php` mendeklarasikan `add_theme_support('custom-logo')`
- [ ] `functions.php` mendeklarasikan `register_nav_menus()` dengan lokasi yang sesuai
- [ ] `functions.php` mendeklarasikan `add_theme_support('post-thumbnails')`
- [ ] Warna dan font di `tailwind.css` diambil dari `DESIGN.md` (tidak ada nilai inventif)

### Template Parts
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
- [ ] `header.php` (logo via `the_custom_logo()`, nav via `wp_nav_menu()`)
- [ ] `footer.php`
- [ ] `single.php` (single post)
- [ ] `page.php` (single page statis)
- [ ] `archive.php` (archive kategori)
- [ ] `search.php`
- [ ] `404.php`

### Verifikasi Elemen Dinamis (Critical)
- [ ] **Tidak ada** hardcode HTML navigasi — semua `wp_nav_menu()`
- [ ] **Tidak ada** hardcode `<img>` untuk logo — semua `the_custom_logo()`
- [ ] **Tidak ada** hardcode ID/slug artikel — semua `WP_Query`
- [ ] **Tidak ada** Tailwind CDN di `header.php` atau `functions.php`
- [ ] Semua output PHP di-escape (`esc_html()`, `esc_url()`, `wp_kses_post()`)

### Checklist Anti-Slop UI
- [ ] Palet warna berasal dari `DESIGN.md`, bukan default AI
- [ ] Tidak ada gradien biru-ungu generik tanpa justifikasi di `DESIGN.md`
- [ ] Layout mobile (375px) sudah diuji secara terpisah
- [ ] Kontras warna teks sudah diverifikasi (min 4.5:1 untuk body text)
- [ ] Tidak ada elemen dinamis/animasi yang berjalan tanpa trigger user

### Finalisasi
- [ ] Screenshot 1200x900px homepage disimpan sebagai `theme/screenshot.png`
- [ ] `npm run bundle` berhasil dijalankan
- [ ] File `.zip` ada di root `.workspaces/` (bukan di dalam `theme-src/`)
- [ ] File `.zip` **tidak ada** di dalam `theme-src/`
- [ ] `.workspaces/THEME_SPECS.md` sudah digenerate

**✅ FASE 3 SELESAI:** `{{ Tanggal }}`

---

## Fase 4: QA (@qa)

- [ ] Lighthouse Performa >= 80
- [ ] Lighthouse SEO >= 80
- [ ] Lighthouse Aksesibilitas >= 80
- [ ] Tidak ada broken link di navigasi dan footer
- [ ] Tampilan mobile (375px) — tidak ada horizontal scroll, tap target >= 44px
- [ ] Tampilan tablet (768px)
- [ ] Tampilan desktop (1280px)
- [ ] Sitemap XML tersedia dan dapat diakses

**✅ FASE 4 SELESAI:** `{{ Tanggal }}`

---

## Fase 5: Deployment (Manusia)

- [ ] Backup pre-deploy tersimpan
- [ ] File tema `.zip` di-upload manual ke `wp-admin → Appearance → Themes → Upload`
- [ ] Tema diaktifkan dan site diperiksa secara visual
- [ ] Post-launch check: homepage, artikel contoh, halaman statis, sitemap

**✅ PROYEK SELESAI:** `{{ Tanggal }}`

---

## Catatan Proyek

`{{ Catat hambatan, keputusan desain, atau perubahan dari rencana awal di sini }}`
