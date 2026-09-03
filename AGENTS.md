# AGENTS.md

## Project Overview

Repo ini adalah **Starter Kit** untuk produksi massal website niche blog/editorial berbasis WordPress. Setiap proyek baru dimulai dengan meng-clone repo ini, mengisi `SITE.md` dan `DESIGN.md`, lalu menjalankan workflow di bawah. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun.

Struktur baku setiap website yang dihasilkan: header menu kategori, homepage hero grid + block per kategori + trending, sidebar opsional, footer latest article, halaman statis, single post/page, archive kategori, search, 404.

## Tech Stack

WordPress (PHP 8.2+), classic theme + Tailwind CSS. Koneksi AI ke situs via WPVibe MCP. AI client: Antigravity.

## Agents

- **@architect** - baca SITE.md & DESIGN.md, susun rencana struktur & wireframe. Tidak menulis kode.
- **@content** - generate kategori, halaman statis, logo/favicon, draft artikel awal.
- **@engineer** - bangun tema classic + Tailwind lewat draft-safe theme builder WPVibe.
- **@qa** - audit Lighthouse, broken link, responsivitas sebelum promosi ke produksi.

## Standard Operating Procedure (SOP)

Urutan kerja wajib diikuti secara berurutan. Jangan loncat fase. **Patuhi Guardrails pada tiap fase dengan ketat!**

**ATURAN UMUM PROGRESS:** Setiap kali satu tugas atau fase selesai, agen **WAJIB seketika itu juga (real-time)** mencatatnya ke dalam `.workspaces/PROGRESS.md`. Jangan menunggu sampai akhir proyek.

1. **Setup (Manusia & Agen):** Clone repo ini, isi `SITE.md` & `DESIGN.md`. *(Catatan: Panggil skill `editorial-brainstorm` jika butuh bantuan AI untuk merumuskan niche, branding, dan sistem desain dari nol).*
   - **GUARDRAIL SETUP:** 
     - Agen **WAJIB** membuat folder wajib `.workspaces/assets/` di awal inisialisasi sebagai tempat menyimpan gambar (logo), featured image, placeholder, dll yang akan diunggah ke website.
     - Segera inisialisasi file `.workspaces/PROGRESS.md`.
     - Agen **WAJIB** menjalankan `wp rewrite structure '/%postname%/'` (via WPVibe) untuk menghapus `index.php`.
     - Agen **WAJIB** menginstal dan mengaktifkan tema **GeneratePress** (`wp theme install generatepress --activate`) di awal proyek. Tema ini digunakan sebagai kanvas netral untuk memvalidasi kesiapan konten.
     - Agen **WAJIB** me-rename nama tema kustom di `package.json` dan `file-header.css` sesuai dengan nama situs di `SITE.md`. Jangan gunakan nama boilerplate `_tw`.

2. **Fase Konten (@content):** 
   - **GUARDRAIL KONTEN:** **DILARANG KERAS** membuat konten *dummy* hanya dalam bentuk file lokal/teks. Agen **WAJIB** menggunakan WPVibe MCP (REST API atau WP-CLI) untuk menginjeksi artikel SEO final, halaman statis (Tentang Kami, dll), dan struktur kategori **langlangsung** ke database server remote.
   - **HARD GATE (VALIDASI KONTEN):** Setelah semua artikel, kategori, tag, halaman statis, dan navigasi menu selesai diunggah, minta Manusia (User) untuk meninjau website secara visual. Karena tema yang aktif adalah GeneratePress, Manusia bisa dengan mudah memastikan seluruh struktur data (konten) sudah benar-benar siap dan masuk ke database. Pengembangan tema kustom **DILARANG** dimulai sebelum ada persetujuan "Konten Siap" dari Manusia.

3. **Fase Tema (@architect -> @engineer):** Hanya boleh dimulai **SETELAH** fase konten selesai dan divalidasi.
   - **GUARDRAIL TEMA (DINAMIS):** **DILARANG** melakukan *hardcode* HTML statis untuk navigasi, menu, tag, atau pencarian. Semua elemen dinamis wajib langsung disambungkan dengan native WordPress functions (`wp_nav_menu()`, `get_tags()`, `has_custom_logo()`) sejak baris kode pertama. File `functions.php` **wajib** mendeklarasikan `add_theme_support('custom-logo')`.
   - **GUARDRAIL BUNDLING:** Ketika menjalankan `npm run bundle`, pastikan script zip dikonfigurasi agar meletakkan output `.zip` di luar struktur source tema (di root `.workspaces/`), **jangan campurkan file zip dengan file source tema**.
   - **GUARDRAIL HANDOVER:** Setelah tema selesai dan di-bundle, agen **WAJIB** meng-generate file `.workspaces/THEME_SPECS.md` yang berisi spesifikasi arsitektur teknis dari tema yang baru dibangun (hierarki kontainer Tailwind, logic custom JS, dll) sebagai dokumen referensi mutlak untuk sesi AI di masa depan.

4. **Fase QA (@qa):** Audit Lighthouse >=80 (performa & SEO), broken link check, uji responsivitas.

5. **Deployment (Manusia):** Karena zip sudah dipisahkan ke luar root source tema, Manusia bisa langsung mengunggah file ZIP tersebut secara manual. Tidak perlu paksakan upload via API/agen jika tidak stabil.

## Workspace

Semua file yang dibuat oleh agent (draft, hasil generate, catatan kerja, aset, output proses) **wajib disimpan di dalam folder `.workspaces/`** di root repo.
- **`.workspaces/assets/`**: Direktori wajib untuk logo, ilustrasi, dummy thumbnail, dan aset visual lainnya.
- **`.workspaces/THEME_SPECS.md`**: Dokumen handover teknis tema saat ini.
- Jangan membuat file baru di luar `.workspaces/` kecuali file tersebut dimaksudkan untuk update repo inti.

## Conventions

Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.

## WPVibe MCP

WPVibe MCP bisa terhubung ke banyak situs WordPress sekaligus. Untuk mencegah kesalahan target, ikuti aturan berikut:

1. **Baca field URL di `SITE.md` terlebih dahulu.** Nilai URL tersebut adalah satu-satunya situs yang boleh dioperasikan.
2. **Jika field URL masih placeholder `{{ }}`**, jangan lakukan operasi WPVibe apa pun.
3. **Jika URL sudah terisi**, validasi bahwa situs tersebut merespons melalui WPVibe sebelum menjalankan operasi pertama. 

## Boundaries (Jangan Lakukan)

- Jangan ubah wp-login atau pengaturan inti wp-admin tanpa persetujuan eksplisit.
- Jangan gunakan FSE block theme penuh atau page builder berat (Elementor/Divi) sebagai basis tema.
- Jangan operasikan situs WordPress mana pun selain yang tercantum di field URL `SITE.md`.
- WordPress berada di server remote. Seluruh interaksi ke WordPress **wajib** dilakukan melalui WPVibe MCP.

## Definition of Done

Kategori & halaman statis terisi (via DB), draft tema disetujui (dinamis & responsif), Lighthouse >=80, permalink beres, file zip terpisah, THEME_SPECS.md ter-generate, backup pra-publish terverifikasi.

## Changelog

Catat setiap pekerjaan yang selesai di repo ini. Entri terbaru di atas.

### `01. 2026-09-03`

- Integrasi aturan Real-time Progress Tracking, Workspace Assets, Strict Dynamic Element, Auto-rename Theme, Hard-Gate Content Validation (GeneratePress), dan THEME_SPECS.md Handover Document.
