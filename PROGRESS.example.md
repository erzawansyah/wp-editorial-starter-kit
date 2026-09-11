# PROGRESS.md - Tracker Progres Proyek

Salin file ini ke `.workspaces/PROGRESS.md` saat memulai proyek baru.
Update checklist ini secara **real-time** setiap kali satu item selesai dikerjakan.
**File ini adalah sumber kebenaran utama untuk melanjutkan pekerjaan di sesi baru.**

---

**Proyek:** `{{ Nama Website }}`
**URL Target:** `{{ URL WordPress }}`
**Dimulai:** `{{ YYYY-MM-DD }}`
**Target selesai:** `{{ YYYY-MM-DD }}`
**Fase Aktif Saat Ini:** `{{ Setup / PRD / Konten / Tema / QA / Deployment }}`

---

## Fase 1: Setup & Environment (Manusia & Agen)

- [ ] Clone repo starter kit
- [ ] Buat direktori wajib `.workspaces/assets/`
- [ ] Buat file `.env` dari `.env.example` berisi `WP_USERNAME` dan `WP_APP_PASSWORD`
- [ ] Isi `SITE.md` tanpa placeholder `{{ }}` yang tersisa _(opsional dibantu skill `wpsk-editorial-brainstorm`)_
- [ ] Isi `DESIGN.md` tanpa placeholder `{{ }}` yang tersisa _(opsional dibantu skill `wpsk-editorial-brainstorm`)_
- [ ] Selesaikan semua item di `WORDPRESS-SETUP.md`
- [ ] Koneksi WP REST API terverifikasi (`GET /wp-json/wp/v2/users/me`)
- [ ] Permalink diatur ke `/%postname%/` _(bisa via wp-admin atau CLI `wp-wpcli-and-ops`)_
- [ ] Salin file ini ke `.workspaces/PROGRESS.md` dan isi metadata di atas

**✅ FASE 1 SELESAI:** `{{ Tanggal }}`

---

## Fase 2: Perencanaan Arsitektur & PRD (@architect)

- [ ] Analisis niche dan persyaratan desain dari `SITE.md` & `DESIGN.md` _(merujuk `wpsk-theme-craft` [perintah `shape`])_
- [ ] Buat dokumen PRD di `PRODUCT.md` (pastikan masuk `.gitignore`)
- [ ] Definisikan daftar seluruh template (`front-page.php`, `single.php`, `author.php` [WAJIB], `page.php`, `archive.php`, dll. merujuk `wpsk-theme-convention`)
- [ ] Susun struktur wireframe detail untuk **Frontpage** (Wajib variasi layout section per kategori: Hero Grid 1+3, 3-column cards, split lead list, trending 1-5, dan pagination ke archive)
- [ ] Susun struktur wireframe detail untuk **Single Article** (Post header, Tombol bagikan social share 6 kanal, Author bio box lengkap, Comment box ter-styling Tailwind, Custom sidebar komponen, Gutenberg layout)
- [ ] Susun struktur wireframe detail untuk **Author Archive (`author.php`)** (Header profil penulis + grid arsip artikel)
- [ ] Rancang container Header yang aman untuk logo gambar (`max-h-12 md:max-h-14`) maupun fallback site title teks

---

> ## ⛔ HARD GATE: VALIDASI PRD OLEH USER
>
> Agen **WAJIB BERHENTI** di sini dan meminta user meninjau dokumen `PRODUCT.md`. Fase berikutnya **tidak boleh dimulai** sebelum baris di bawah ini terisi dan disetujui.
>
> **Status:** `[ ] MENUNGGU PERSETUJUAN` → `[ ] DISETUJUI oleh user pada {{ Tanggal }}`
>
> **Catatan review user:** `{{ Catat masukan atau revisi wireframe dari user di sini }}`

---

**✅ FASE 2 SELESAI & HARD GATE DILEWATI:** `{{ Tanggal }}`

---

## Fase 3: Fondasi Konten, Penulis, & Menu Navigasi (@content)

> **PRINSIP CONTENT-FIRST:**
> Fase ini diselesaikan **sebelum** tema dibangun agar tema terhubung ke data nyata.

### Pembuatan User Author via WP REST API (Diversitas Nama)

- [ ] 3–5 akun user dengan role `author` berhasil dibuat via REST API
- [ ] Nama author dipastikan beragam dan realistis (Jawa, Sunda, Minang, Batak, Melayu, Timur) — **bebas dari nama klise repetitif seperti Dimas atau Pramesti**
- [ ] Format email diverifikasi: `<username>@<site.com>` untuk setiap author
- [ ] Setiap author memiliki bio profil realistis 2–3 kalimat sesuai beat liputannya
- [ ] Daftar ID author dicatat untuk rotasi penulisan artikel

### Taksonomi, Menu Navigasi, & Halaman Statis via WP REST API

- [ ] Kategori dibuat via REST API (`POST /wp-json/wp/v2/categories`) sesuai `PRODUCT.md`
- [ ] Tag utama dibuat via REST API (`POST /wp-json/wp/v2/tags`)
- [ ] Struktur Menu Navigasi Header (Primary) dan Footer ditetapkan dan didaftarkan di WordPress
- [ ] Halaman statis format Gutenberg dibuat via REST API _(merujuk `wp-patterns`)_ (Tentang Kami, Tim Redaksi, Kontak, Privasi, Pedoman Media Siber)

### Aset Visual & Branding

- [ ] Logo situs (SVG & PNG) diunggah ke Media Library
- [ ] Favicon (ICO & PNG 192px)
- [ ] OG Image default (1200x630px)
- [ ] Seluruh aset tersimpan rapi di `.workspaces/assets/`

### Penulisan Artikel Paralel via Subagents

- [ ] Pemanggilan subagents secara paralel untuk penulisan artikel
- [ ] Setiap subagent mengeksekusi penulisan artikel merujuk standar skill **`wpsk-seo-writer`** (anti-slop bahasa Indonesia, zero fluff, riset fakta terverifikasi, PAA question H2, tabel terverifikasi)
- [ ] Setiap artikel diformat menggunakan Gutenberg Blocks murni merujuk skill **`wp-patterns`**
- [ ] Featured Image dicari (dapat menggunakan WPVibe `search_images`) dan di-set sebagai post thumbnail via REST API
- [ ] Setiap artikel dipublikasikan via REST API diatribusikan ke author bergantian (**Dilarang keras memakai akun admin**)
- [ ] Minimal 3 artikel per kategori utama berhasil terbit

**✅ FASE 3 SELESAI:** `{{ Tanggal }}`

---

## Fase 4: Pengembangan Tema Kustom (@engineer)

> **FASE INI DIMULAI SETELAH KONTEN & MENU SUDAH TERSEDIA DI WORDPRESS.**

### Prasyarat Teknis & Bacaan Skill

- [ ] Skill `wpsk-theme-convention/SKILL.md` sudah dibaca penuh _(standar arsitektur PHP dinamis)_
- [ ] Skill `wpsk-theme-craft/SKILL.md` sudah dibaca penuh _(Craft Floor, a11y WCAG, mobile reflow, 9 fungsi Impeccable)_
- [ ] _(Opsional)_ Skill `wp-block-development/SKILL.md` dibaca jika situs butuh custom Gutenberg block
- [ ] Dokumen `PRODUCT.md` dan `DESIGN.md` dipatuhi secara mutlak
- [ ] Theme source di-scaffold di `.workspaces/theme-src/` dari underscoretw.com
- [ ] `npm install` berhasil dijalankan
- [ ] `npm run dev` berhasil — `theme/style.css` ter-generate

### Konfigurasi & Fungsi Tema (Merujuk `wpsk-theme-convention`)

- [ ] Nama tema di `theme/style.css` diubah dari `_tw` ke nama situs dari `SITE.md`
- [ ] `functions.php` mendeklarasikan `add_theme_support('custom-logo')` dengan batasan terukur
- [ ] `functions.php` mendeklarasikan `register_nav_menus()` untuk lokasi primary dan footer
- [ ] `functions.php` mendeklarasikan `add_theme_support('post-thumbnails')`
- [ ] Token warna dan tipografi di `tailwind.css` diambil dari `DESIGN.md`

### Implementasi 8 Aturan Baku Tema & Template Parts

- [ ] **Header & Logo Anti-Meluap:** Container logo dibatasi (`max-h-12 md:max-h-14 w-auto object-contain flex-shrink-0`), mendukung logo gambar maupun site title teks tanpa merusak layout
- [ ] **Navigasi Dinamis:** Tidak ada link navigasi yang di-hardcode — semua memakai `wp_nav_menu()`
- [ ] **Frontpage Multi-Style:** `front-page.php` memiliki variasi section layout per kategori (Hero Grid 1+3, 3-column cards, split list, trending 1-5)
- [ ] **Frontpage Pagination:** Tombol/navigasi pagination mengarah ke Archive Page spesifik
- [ ] **Single Post Lengkap:** `single.php` memuat Author Box (`get_avatar()`, bio, link arsip), Comment Box ter-styling Tailwind penuh, dan Custom Sidebar komponen
- [ ] **Tombol Bagikan Social Share (6 Kanal):** `template-parts/post/social-share.php` dibuat (WhatsApp, Telegram, Facebook, X/Twitter, Threads, Copy Link dengan visual feedback)
- [ ] **Custom Sidebar Komponen:** `template-parts/sidebar/sidebar-single.php` dibuat (bio mini, trending posts `WP_Query`, category strip)
- [ ] **Template `author.php` Wajib:** Header profil penulis (avatar besar, bio, count artikel) + grid arsip artikel penulis
- [ ] **Browser Surfaces Styling:** Seleksi teks (`::selection`), focus-visible ring, dan scrollbar distyle rapi _(merujuk `wpsk-theme-craft`)_
- [ ] **Query Dinamis:** Semua data menggunakan `WP_Query` dan `get_categories()`
- [ ] **Anti-Slop & Craft Floor:** Tidak ada nested cards, tidak ada gradien ungu-biru, body measure 65-75ch
- [ ] Semua output PHP di-escape (`esc_html()`, `esc_url()`, `wp_kses_post()`)

### Finalisasi & Serah Terima Tema

- [ ] Screenshot 1200x900px homepage disimpan sebagai `theme/screenshot.png`
- [ ] `npm run bundle` berhasil dijalankan
- [ ] File `.zip` berada di root `.workspaces/` (bukan di dalam `theme-src/`)
- [ ] File `.zip` diserahkan kepada user untuk diunggah/diaktifkan di WordPress
- [ ] Dokumen `.workspaces/THEME_SPECS.md` digenerate

**✅ FASE 4 SELESAI:** `{{ Tanggal }}`

---

## Fase 5: QA, Audit, & Verifikasi Visual (@qa)

### Verifikasi Visual Otomatis (Playwright Screenshot)

- [ ] Playwright membuka URL website live/staging di background
- [ ] **Full-Page Screenshot Desktop (1440px)** diambil (Homepage, Single Post, Author Archive)
- [ ] **Full-Page Screenshot Mobile (375px)** diambil (Homepage, Single Post, Author Archive)
- [ ] Screenshot disematkan langsung di dalam dokumen **Artifact** untuk review visual user

### Audit Teknis & Aksesibilitas (`wpsk-theme-craft`)

- [ ] Script kalkulator kontras dijalankan (`contrast-check.py`) — semua teks lolos min 4.5:1 (WCAG AA)
- [ ] Verifikasi navigasi keyboard (`:focus-visible` ring kontras 3:1)
- [ ] Uji responsivitas mobile (375px) — bebas horizontal scrollbar, tap target >= 44x44px
- [ ] Uji responsivitas tablet (768px) dan desktop (1280px/1440px)
- [ ] Profiling query SQL & optimasi database _(merujuk `wp-performance`)_
- [ ] Lighthouse Performance >= 80 & SEO >= 80
- [ ] Tidak ada broken link di navigasi, konten, dan footer
- [ ] XML Sitemap dapat diakses dan valid

**✅ FASE 5 SELESAI:** `{{ Tanggal }}`

---

## Fase 6: Deployment & Serah Terima (Manusia & Agen)

- [ ] File tema `.zip` terbaru dari `.workspaces/` aktif di WordPress
- [ ] Website langsung tampil utuh, hidup, dan proporsional bersama konten yang sudah diinjeksi
- [ ] Backup pre-deploy tersimpan _(opsional via `wp-wpcli-and-ops`)_
- [ ] Flush cache dan rewrite rules jika diperlukan _(opsional via `wp-wpcli-and-ops`)_
- [ ] Post-launch check: homepage, single article, author archive, halaman statis, search, 404

**✅ PROYEK SELESAI:** `{{ Tanggal }}`

---

## Catatan Proyek

`{{ Catat hambatan, keputusan desain, atau perubahan dari rencana awal di sini }}`
