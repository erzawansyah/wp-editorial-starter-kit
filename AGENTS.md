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

## Sesi Lintas Session — Cara Melanjutkan Pekerjaan

> **WAJIB DIBACA DI AWAL SETIAP SESI BARU:**

1. **Baca SITE.md.** Jika ada field `{{ }}` yang belum terisi, **BERHENTI** dan tanyakan ke user sebelum melakukan apapun.
2. **Baca `.workspaces/PROGRESS.md`.** Dokumen ini adalah satu-satunya sumber kebenaran tentang posisi proyek saat ini. Identifikasi fase terakhir yang selesai dan lanjutkan dari sana. **Jangan pernah mengulang fase yang sudah selesai tanpa izin user.**
3. **Verifikasi fase aktif.** Sebelum mengerjakan tugas apa pun, nyatakan secara eksplisit ke user: "Saya melanjutkan dari [nama fase] — saya akan [tindakan berikutnya]." Tunggu konfirmasi singkat jika ada perubahan dari ekspektasi.
4. **Jangan asumsikan — verifikasi.** Jika `.workspaces/PROGRESS.md` tidak ada, buat terlebih dahulu sebelum melanjutkan.

## Standard Operating Procedure (SOP)

Urutan kerja wajib diikuti secara berurutan. Jangan loncat fase. **Patuhi Guardrails pada tiap fase dengan ketat!**

**ATURAN UMUM PROGRESS:** Setiap kali satu tugas atau fase selesai, agen **WAJIB seketika itu juga (real-time)** mencatatnya ke dalam `.workspaces/PROGRESS.md`. Jangan menunggu sampai akhir proyek.

---

### Fase 1: Setup (Manusia & Agen)

Clone repo ini, isi `SITE.md` & `DESIGN.md`. *(Catatan: Panggil skill `wpsk-editorial-brainstorm` jika butuh bantuan AI untuk merumuskan niche, branding, dan sistem desain dari nol).*

**GUARDRAILS SETUP:**

- Agen **WAJIB** membuat folder wajib `.workspaces/assets/` di awal inisialisasi sebagai tempat menyimpan gambar (logo), featured image, placeholder, dll yang akan diunggah ke website.
- Segera inisialisasi file `.workspaces/PROGRESS.md` menggunakan template dari `PROGRESS.example.md`.
- Agen **WAJIB** menjalankan `wp rewrite structure '/%postname%/'` (via WPVibe) untuk menghapus `index.php`.
- Agen **WAJIB** menginstal dan mengaktifkan tema **GeneratePress** (`wp theme install generatepress --activate`) di awal proyek. Tema ini digunakan sebagai kanvas netral untuk memvalidasi kesiapan konten.
- Agen **WAJIB** memverifikasi bahwa `DESIGN.md` terisi penuh — tidak ada field `{{ }}` yang tersisa.

---

### Fase 2: Konten (@content)

**GUARDRAIL PENULISAN (SEO):** Saat membuat draf artikel atau *copywriting* halaman statis, agen **WAJIB** merujuk pada instruksi dari skill `seo-article` untuk memastikan tulisan memiliki standar SEO yang tinggi, kaya akan data riset, dan tidak terdengar seperti konten AI generik (*slop*).

**GUARDRAIL KONTEN:** **DILARANG KERAS** membuat konten *dummy* hanya dalam bentuk file lokal/teks. Agen **WAJIB** menggunakan WPVibe MCP (REST API atau WP-CLI) untuk menginjeksi artikel SEO final, halaman statis (Tentang Kami, dll), dan struktur kategori **langsung** ke database server remote.

**GUARDRAIL FORMAT (GUTENBERG & MEDIA):** Seluruh artikel dan halaman yang diunggah **WAJIB** diformat menggunakan struktur sintaks *Gutenberg Blocks* murni (agen dapat merujuk pada panduan sintaksis blok di dalam skill `wp-patterns`), **DILARANG KERAS** menggunakan HTML mentah (*classic block*). Selain itu, agen **WAJIB** meng-generate *Featured Image* dan menetapkannya (set *post thumbnail*) untuk setiap artikel yang dipublikasikan.

**HARD GATE (VALIDASI KONTEN):** Setelah semua artikel, kategori, tag, halaman statis, dan navigasi menu selesai diunggah, minta Manusia (User) untuk meninjau website secara visual. Karena tema yang aktif adalah GeneratePress, Manusia bisa dengan mudah memastikan seluruh struktur data (konten) sudah benar-benar siap dan masuk ke database. Pengembangan tema kustom **DILARANG** dimulai sebelum ada persetujuan "Konten Siap" dari Manusia. **Catat persetujuan ini di `.workspaces/PROGRESS.md`.**

---

### Fase 3: Tema (@architect → @engineer)

> **FASE INI HANYA BOLEH DIMULAI SETELAH:**
> 1. Baris "HARD GATE: Konten disetujui" sudah tertulis di `.workspaces/PROGRESS.md`
> 2. `DESIGN.md` tidak memiliki field `{{ }}` yang tersisa

**INSTRUKSI PERTAMA @engineer:** Sebelum menulis kode apapun, **baca dulu** skill `wpsk-theme-convention` (`.agents/skills/wpsk-theme-convention/SKILL.md`) secara lengkap. Skill itu adalah spesifikasi teknis yang mengikat — bukan sekadar panduan.

**GUARDRAIL SKILLS (UI/UX):** Saat mulai merancang atau membangun UI tema, agen **WAJIB** membaca dan menerapkan instruksi dari tiga skill berikut secara berurutan:

1. `antislop-ui` — filter utama anti-slop visual
2. `antislop-human` — aksesibilitas dan kontras warna
3. `antislop-layoutmobile` — responsivitas dan layout mobile
4. `frontend-design` — art direction dan tipografi editorial yang distinctive

**GUARDRAIL DESAIN (STRICT DESIGN.md):** `DESIGN.md` adalah **Sumber Kebenaran Mutlak (Single Source of Truth)**. Agen **DILARANG KERAS** mengubah isi dokumen `DESIGN.md` yang sudah ditentukan tanpa izin eksplisit dari user. Seluruh implementasi harus tunduk pada spesifikasi di dalam dokumen tersebut.

**GUARDRAIL TEMA (DINAMIS — TIDAK ADA PENGECUALIAN):**
- **DILARANG** hardcode HTML statis untuk navigasi → wajib `wp_nav_menu()`
- **DILARANG** hardcode `<img>` untuk logo → wajib `the_custom_logo()`
- **DILARANG** hardcode ID/slug artikel → wajib `WP_Query`
- **DILARANG** hardcode teks kategori → wajib `get_categories()`
- **DILARANG** gunakan Tailwind CDN → wajib build pipeline PostCSS lokal
- `functions.php` **wajib** mendeklarasikan `add_theme_support('custom-logo')` dan `register_nav_menus()`

**GUARDRAIL BUILD:**
- Semua coding tema dilakukan **secara lokal** di `.workspaces/theme-src/`
- **DILARANG** menggunakan WPVibe untuk menulis atau mengedit file PHP/CSS/JS tema
- **JANGAN EDIT MANUAL** file `theme/style.css` atau `theme/js/` — ini adalah output build
- Jalankan `npm run dev` setelah setiap batch perubahan untuk verifikasi

**GUARDRAIL SCREENSHOT:** Setelah tema *final*, agen atau manusia **WAJIB** membuat screenshot berukuran 1200x900px dari Homepage dan menyimpannya sebagai `theme/screenshot.png` di dalam source tema.

**GUARDRAIL BUNDLING:** Output `.zip` dari `npm run bundle` **wajib** berada di root `.workspaces/`, **bukan** di dalam `theme-src/`. Pastikan `package.json` dikonfigurasi untuk ini.

**GUARDRAIL HANDOVER:** Setelah tema selesai dan di-bundle, agen **WAJIB** meng-generate file `.workspaces/THEME_SPECS.md` yang berisi spesifikasi arsitektur teknis tema sebagai dokumen referensi mutlak untuk sesi AI di masa depan.

**CHECKLIST WAJIB SEBELUM BUNDLE:** Jalankan seluruh checklist di `wpsk-theme-convention/SKILL.md` bagian "Checklist Fase Tema". Semua item harus ✅ sebelum `npm run bundle` dijalankan.

---

### Fase 4: QA (@qa)

Audit Lighthouse >=80 (performa & SEO), broken link check, uji responsivitas di mobile (375px), tablet (768px), desktop (1280px).

---

### Fase 5: Deployment (Manusia)

Karena zip sudah dipisahkan ke luar root source tema, Manusia bisa langsung mengunggah file ZIP tersebut secara manual ke `wp-admin → Appearance → Themes → Add New → Upload Theme`. Tidak perlu paksakan upload via API/agen jika tidak stabil.

---

## Workspace

Semua file yang dibuat oleh agent (draft, hasil generate, catatan kerja, aset, output proses) **wajib disimpan di dalam folder `.workspaces/`** di root repo dengan struktur yang rapi:

- **`.workspaces/assets/`** — logo, ilustrasi, thumbnail, dan aset visual lainnya.
- **`.workspaces/theme-src/`** — source code tema (PHP, CSS, JS, `package.json`). Tidak ada yang lain di sini.
- **`.workspaces/scripts/`** — skrip eksekusi sementara atau tools automation (`.js`, `.py`, `.sh`).
- **`.workspaces/temp/`** — file temporer (scratch, log error, dump JSON). Tidak perlu dipertahankan.
- **`.workspaces/THEME_SPECS.md`** — dokumen handover teknis tema.
- **`.workspaces/PROGRESS.md`** — dokumen pelacakan progres proyek (real-time).

**Aturan Ketat:**
- **DILARANG KERAS** menumpuk file campuran langsung di root `.workspaces/`. Kelompokkan ke subfolder yang tepat.
- **DILARANG** membuat file baru di luar `.workspaces/` kecuali untuk mengupdate template inti (`AGENTS.md`, `README.md`, atau file example).

## Conventions

Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.

**Aturan Pembuatan Skill Baru:** Jika agen atau manusia membuat custom skill spesifik untuk ekosistem *Starter Kit* ini, nama folder dan `name:` di YAML *wajib* menggunakan awalan `wpsk-` (WordPress Starter Kit). Contoh: `wpsk-editorial-brainstorm`, `wpsk-theme-convention`.

## Skill UI yang Aktif (Fase Tema)

Daftar skill UI yang **wajib digunakan** di fase tema, berurutan sesuai prioritas. Tidak ada skill lain di luar daftar ini yang diizinkan untuk UI work:

| Prioritas | Skill | Kapan Digunakan |
|---|---|---|
| 1 | `antislop-ui` | Selalu — filter utama semua UI work |
| 2 | `antislop-human` | Selalu — aksesibilitas, kontras, keyboard |
| 3 | `antislop-layoutmobile` | Selalu — layout responsif mobile |
| 4 | `frontend-design` | Saat menentukan arah estetika & tipografi |

## WPVibe MCP

WPVibe MCP bisa terhubung ke banyak situs WordPress sekaligus. Untuk mencegah kesalahan target, ikuti aturan berikut:

1. **Baca field URL di `SITE.md` terlebih dahulu.** Nilai URL tersebut adalah satu-satunya situs yang boleh dioperasikan.
2. **Jika field URL masih placeholder `{{ }}`**, jangan lakukan operasi WPVibe apa pun.
3. **Jika URL sudah terisi**, validasi bahwa situs tersebut merespons melalui WPVibe sebelum menjalankan operasi pertama.

## Boundaries (Jangan Lakukan)

- Jangan ubah wp-login atau pengaturan inti wp-admin tanpa persetujuan eksplisit.
- Jangan gunakan FSE block theme penuh atau page builder berat (Elementor/Divi) sebagai basis tema.
- Jangan operasikan situs WordPress mana pun selain yang tercantum di field URL `SITE.md`.
- WordPress berada di server remote. Seluruh interaksi ke WordPress **wajib** dilakukan melalui WPVibe MCP — kecuali penulisan kode tema (lokal).
- Jangan mulai Fase Tema sebelum `.workspaces/PROGRESS.md` mencatat persetujuan Hard-Gate Konten dari user.
- Jangan gunakan Tailwind CDN untuk tema. Build pipeline PostCSS adalah satu-satunya cara.

## Definition of Done

Kategori & halaman statis terisi (via DB), draft tema disetujui (dinamis & responsif), Lighthouse >=80, permalink beres, file zip terpisah di root `.workspaces/`, THEME_SPECS.md ter-generate, screenshot.png tersedia, backup pra-publish terverifikasi.

## Changelog

Catat setiap pekerjaan yang selesai di repo ini. Entri terbaru di atas.

### `03. 2026-09-08`

- **Sinkronisasi Dokumen:** Rewrite total `wpsk-theme-convention/SKILL.md` agar selaras 100% dengan `AGENTS.md` — menghapus instruksi WPVibe yang kontradiktif, menambahkan prasyarat Hard-Gate dan DESIGN.md check, memperjelas arsitektur source vs output, menambahkan aturan elemen dinamis eksplisit dengan kode contoh, dan checklist wajib sebelum bundling.
- **Efisiensi Skill UI:** Menghapus 5 skill UI yang tidak relevan atau tumpang tindih (`baseline-ui`, `web-design-guidelines`, `wpds`, `ui-ux-pro-max`, `impeccable`). Hanya menyisakan 4 skill UI terintegrasi: `antislop-ui`, `antislop-human`, `antislop-layoutmobile`, `frontend-design`.
- **Enforcement Lintas Sesi:** Menambahkan seksi "Sesi Lintas Session" di `AGENTS.md` yang mewajibkan agen membaca `PROGRESS.md` terlebih dahulu sebelum bekerja, mencegah pengulangan fase dan inkonsistensi antar sesi.
- **Guardrail Tema yang Diperkuat:** Memperjelas setiap guardrail fase tema dengan perintah spesifik (dinamis vs hardcode, build pipeline, lokasi output zip, urutan baca skill).

### `02. 2026-09-05`

- **Generic Rebranding:** Menghapus seluruh referensi spesifik "Croco" untuk menjadikannya *starter kit* netral.
- **Strict Local Theme:** Menegaskan pengembangan tema secara luring di folder `.workspaces/theme-src/` tanpa memodifikasi *live site* via WPVibe.
- **Workspace Architecture:** Merapikan dan meratakan (*flatten*) struktur folder `.workspaces/` dengan sub-direktori spesifik (`/temp`, `/scripts`, `/assets`) untuk mencegah penumpukan file.
- **Content Guardrails:** Mewajibkan penggunaan skill `seo-article` untuk standar SEO, serta `wp-patterns` untuk memastikan seluruh unggahan artikel menggunakan sintaks murni *Gutenberg Blocks* berikut *Featured Image*.

### `01. 2026-09-03`

- Integrasi aturan Real-time Progress Tracking, Workspace Assets, Strict Dynamic Element, Auto-rename Theme, Hard-Gate Content Validation (GeneratePress), dan THEME_SPECS.md Handover Document.
