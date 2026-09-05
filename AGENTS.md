# AGENTS.md

## Project Overview

Repo ini adalah **Starter Kit** untuk produksi massal website niche blog/editorial berbasis WordPress. Setiap proyek baru dimulai dengan meng-clone repo ini, mengisi `SITE.md` dan `DESIGN.md`, lalu menjalankan workflow di bawah. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun.

Struktur baku setiap website yang dihasilkan: header menu kategori, homepage hero grid + block per kategori + trending, sidebar opsional, footer latest article, halaman statis, single post/page, archive kategori, search, 404.

## Tech Stack

WordPress (PHP 8.2+), classic theme + Tailwind CSS. Koneksi AI ke situs via WPVibe MCP. AI client: Antigravity.

## Agents

- **@architect** - baca SITE.md & DESIGN.md, susun rencana struktur & wireframe. Tidak menulis kode.
- **@content** - generate kategori, halaman statis, logo/favicon, draft artikel awal.
- **@engineer** - bangun tema classic + Tailwind secara lokal di dalam folder workspaces (tanpa WPVibe).
- **@qa** - audit Lighthouse, broken link, responsivitas sebelum promosi ke produksi.

## Standard Operating Procedure (SOP)

Urutan kerja wajib diikuti secara berurutan. Jangan loncat fase. **Patuhi Guardrails pada tiap fase dengan ketat!**

**ATURAN UMUM PROGRESS:** Setiap kali satu tugas atau fase selesai, agen **WAJIB seketika itu juga (real-time)** mencatatnya ke dalam `.workspaces/PROGRESS.md`. Jangan menunggu sampai akhir proyek.

1. **Setup (Manusia & Agen):** Clone repo ini, isi `SITE.md` & `DESIGN.md`. *(Catatan: Panggil skill `wpsk-editorial-brainstorm` jika butuh bantuan AI untuk merumuskan niche, branding, dan sistem desain dari nol).*
   - **GUARDRAIL SETUP:** 
     - Agen **WAJIB** membuat folder wajib `.workspaces/assets/` di awal inisialisasi sebagai tempat menyimpan gambar (logo), featured image, placeholder, dll yang akan diunggah ke website.
     - Segera inisialisasi file `.workspaces/PROGRESS.md`.
     - Agen **WAJIB** menjalankan `wp rewrite structure '/%postname%/'` (via WPVibe) untuk menghapus `index.php`.
     - Agen **WAJIB** menginstal dan mengaktifkan tema **GeneratePress** (`wp theme install generatepress --activate`) di awal proyek. Tema ini digunakan sebagai kanvas netral untuk memvalidasi kesiapan konten.
     - Agen **WAJIB** me-rename nama tema kustom di `package.json` dan `file-header.css` sesuai dengan nama situs di `SITE.md`. Jangan gunakan nama boilerplate `_tw`.

2. **Fase Konten (@content):** 
   - **GUARDRAIL PENULISAN (SEO):** Saat membuat draf artikel atau *copywriting* halaman statis, agen **WAJIB** merujuk pada instruksi dari skill `seo-article` untuk memastikan tulisan memiliki standar SEO yang tinggi, kaya akan data riset, dan tidak terdengar seperti konten AI generik (*slop*).
   - **GUARDRAIL KONTEN:** **DILARANG KERAS** membuat konten *dummy* hanya dalam bentuk file lokal/teks. Agen **WAJIB** menggunakan WPVibe MCP (REST API atau WP-CLI) untuk menginjeksi artikel SEO final, halaman statis (Tentang Kami, dll), dan struktur kategori **langsung** ke database server remote.
   - **GUARDRAIL FORMAT (GUTENBERG & MEDIA):** Seluruh artikel dan halaman yang diunggah **WAJIB** diformat menggunakan struktur sintaks *Gutenberg Blocks* murni (agen dapat merujuk pada panduan sintaksis blok di dalam skill `wp-patterns`), **DILARANG KERAS** menggunakan HTML mentah (*classic block*). Selain itu, agen **WAJIB** meng-generate *Featured Image* dan menetapkannya (set *post thumbnail*) untuk setiap artikel yang dipublikasikan.
   - **HARD GATE (VALIDASI KONTEN):** Setelah semua artikel, kategori, tag, halaman statis, dan navigasi menu selesai diunggah, minta Manusia (User) untuk meninjau website secara visual. Karena tema yang aktif adalah GeneratePress, Manusia bisa dengan mudah memastikan seluruh struktur data (konten) sudah benar-benar siap dan masuk ke database. Pengembangan tema kustom **DILARANG** dimulai sebelum ada persetujuan "Konten Siap" dari Manusia.

3. **Fase Tema (@architect -> @engineer):** Hanya boleh dimulai **SETELAH** fase konten selesai dan divalidasi.
   - **GUARDRAIL SKILLS (UI/UX):** Saat mulai merancang atau membangun UI tema, agen **WAJIB** merujuk dan menerapkan instruksi dari skill desain yang ada di repo (seperti `antislop-ui`, `ui-ux-pro-max`, `baseline-ui`, atau `frontend-design`) untuk memastikan UI yang dihasilkan berkualitas tinggi dan tidak terkesan *slop*.
   - **GUARDRAIL DESAIN (STRICT DESIGN.md):** `DESIGN.md` adalah **Sumber Kebenaran Mutlak (Single Source of Truth)**. Selama evaluasi desain maupun pembangunan tema, agen **DILARANG KERAS** mengubah isi dokumen `DESIGN.md` yang sudah ditentukan tanpa izin eksplisit dari *user*. Seluruh implementasi harus tunduk pada spesifikasi di dalam dokumen tersebut.
   - **GUARDRAIL TEMA (DINAMIS):** **DILARANG** melakukan *hardcode* HTML statis untuk navigasi, menu, tag, atau pencarian. Semua elemen dinamis wajib langsung disambungkan dengan native WordPress functions (`wp_nav_menu()`, `get_tags()`, `has_custom_logo()`) sejak baris kode pertama. File `functions.php` **wajib** mendeklarasikan `add_theme_support('custom-logo')`.
   - **GUARDRAIL SCREENSHOT:** Apabila tema yang dikembangkan sudah *final*, agen atau manusia **WAJIB** membuat sebuah *screenshot* berukuran 1200x900px dari tampilan website (misal: Homepage) dan menyimpannya sebagai `screenshot.png` (atau `.jpg`) di direktori *root* dari *source code* tema. Ini bertujuan agar tema tersebut terlihat profesional di halaman *dashboard* WordPress (Appearance -> Themes).
   - **GUARDRAIL BUNDLING:** Ketika menjalankan `npm run bundle`, pastikan script zip dikonfigurasi agar meletakkan output `.zip` di luar struktur source tema (di root `.workspaces/`), **jangan campurkan file zip dengan file source tema**.
   - **GUARDRAIL HANDOVER:** Setelah tema selesai dan di-bundle, agen **WAJIB** meng-generate file `.workspaces/THEME_SPECS.md` yang berisi spesifikasi arsitektur teknis dari tema yang baru dibangun (hierarki kontainer Tailwind, logic custom JS, dll) sebagai dokumen referensi mutlak untuk sesi AI di masa depan.

4. **Fase QA (@qa):** Audit Lighthouse >=80 (performa & SEO), broken link check, uji responsivitas.

5. **Deployment (Manusia):** Karena zip sudah dipisahkan ke luar root source tema, Manusia bisa langsung mengunggah file ZIP tersebut secara manual. Tidak perlu paksakan upload via API/agen jika tidak stabil.

## Workspace

Semua file yang dibuat oleh agent (draft, hasil generate, catatan kerja, aset, output proses) **wajib disimpan di dalam folder `.workspaces/`** di root repo dengan struktur yang rapi dan terorganisir:

- **`.workspaces/assets/`**: Direktori wajib untuk logo, ilustrasi, dummy thumbnail, dan aset visual lainnya.
- **`.workspaces/theme-src/`**: Direktori eksklusif untuk *source code* pengembangan tema (PHP, CSS, JS, `package.json`).
- **`.workspaces/scripts/`**: Tempat menyimpan seluruh skrip eksekusi sementara atau *tools automation* (misal `.js`, `.py`, `.sh`) yang dibuat oleh agen untuk mempermudah pekerjaan.
- **`.workspaces/temp/`**: Tempat menyimpan file temporer (*scratch file*, draf tulisan mentah, log *error*, atau *dump* JSON) yang tidak perlu dipertahankan di akhir proyek.
- **`.workspaces/THEME_SPECS.md`**: Dokumen penting serah terima (*handover*) teknis tema.
- **`.workspaces/PROGRESS.md`**: Dokumen penting pelacakan progres proyek.

**Aturan Ketat Folder Workspace:**
- **DILARANG KERAS** menumpuk file campuran (draf konten, log, skrip) langsung di *root* `.workspaces/`. Agen **WAJIB** mengelompokkannya ke dalam sub-folder yang sesuai (`/scripts`, `/temp`, `/assets`, atau `/theme-src`).
- **DILARANG** membuat file baru di luar `.workspaces/` kecuali file tersebut secara spesifik dimaksudkan untuk meng-*update* aturan *core template* dari repositori *Starter Kit* ini (misalnya `AGENTS.md` atau `README.md`).

## Conventions

Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.

**Aturan Pembuatan Skill Baru:** Jika agen atau manusia membuat custom skill spesifik untuk ekosistem *Starter Kit* ini, nama folder dan `name:` di YAML *wajib* menggunakan awalan `wpsk-` (WordPress Starter Kit). Contoh: `wpsk-editorial-brainstorm`, `wpsk-theme-convention`.

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

Kategori & halaman statis terisi (via DB), draft tema disetujui (dinamis & responsif), Lighthouse >=80, permalink beres, file zip terpisah, THEME_SPECS.md ter-generate, screenshot.png tersedia, backup pra-publish terverifikasi.

## Changelog

Catat setiap pekerjaan yang selesai di repo ini. Entri terbaru di atas.

### `02. 2026-09-05`

- **Generic Rebranding:** Menghapus seluruh referensi spesifik "Croco" untuk menjadikannya *starter kit* netral.
- **Strict Local Theme:** Menegaskan pengembangan tema secara luring di folder `.workspaces/theme-src/` tanpa memodifikasi *live site* via WPVibe.
- **Workspace Architecture:** Merapikan dan meratakan (*flatten*) struktur folder `.workspaces/` dengan sub-direktori spesifik (`/temp`, `/scripts`, `/assets`) untuk mencegah penumpukan file.
- **Content Guardrails:** Mewajibkan penggunaan skill `seo-article` untuk standar SEO, serta `wp-patterns` untuk memastikan seluruh unggahan artikel menggunakan sintaks murni *Gutenberg Blocks* berikut *Featured Image*.

### `01. 2026-09-03`

- Integrasi aturan Real-time Progress Tracking, Workspace Assets, Strict Dynamic Element, Auto-rename Theme, Hard-Gate Content Validation (GeneratePress), dan THEME_SPECS.md Handover Document.
