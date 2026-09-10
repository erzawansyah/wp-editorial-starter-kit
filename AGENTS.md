# AGENTS.md

## Project Overview

Repo ini adalah **Starter Kit** untuk produksi massal website niche blog/editorial berbasis WordPress. Setiap proyek baru dimulai dengan meng-clone repo ini, mengisi `.env`, `SITE.md`, dan `DESIGN.md`, lalu menjalankan workflow di bawah. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun.

Struktur baku setiap website yang dihasilkan: header menu kategori, homepage hero grid + block per kategori + trending, sidebar opsional, footer latest article, halaman statis, single post/page, archive kategori, search, 404.

## Tech Stack

WordPress (PHP 8.2+), classic theme + Tailwind CSS. Manajemen konten via WordPress REST API (Basic Auth Application Password dari `.env`). WPVibe MCP digunakan khusus untuk operasi di luar REST API (seperti pencarian gambar/featured image). AI client: Antigravity.

## Agents

- **@architect** - baca `SITE.md` & `DESIGN.md`, susun PRD di `PRODUCT.md` (daftar template & wireframe mendalam terutama frontpage dan single artikel). Mengacu pada `frontend-design` dan `wpsk-theme-convention`. Tidak menulis kode tema.
- **@engineer** - bangun tema classic + Tailwind secara lokal di `.workspaces/theme-src/` mengacu pada `PRODUCT.md`, `DESIGN.md`, dan panduan teknis `wpsk-theme-convention`. Menyerahkan bundle ZIP tema di root `.workspaces/` setiap ada perubahan tema.
- **@content** - kelola konten via WP REST API: buat 3–5 user author, taksonomi, halaman statis (`wp-patterns`), serta memimpin penulisan artikel SEO Gutenberg secara paralel melalui subagent (menggunakan skill `wpsk-seo-writer`).
- **@qa** - audit Lighthouse, performa backend (`wp-performance`), aksesibilitas (`antislop-human`), dan responsivitas (`antislop-layoutmobile`) sebelum promosi ke produksi.

## Sesi Lintas Session — Cara Melanjutkan Pekerjaan

> **WAJIB DIBACA DI AWAL SETIAP SESI BARU:**

1. **Baca SITE.md dan .env.** Jika ada field `{{ }}` di `SITE.md` atau kredensial di `.env` belum terisi, **BERHENTI** dan tanyakan ke user sebelum melakukan apapun.
2. **Baca `.workspaces/PROGRESS.md`.** Dokumen ini adalah satu-satunya sumber kebenaran tentang posisi proyek saat ini. Identifikasi fase terakhir yang selesai dan lanjutkan dari sana. **Jangan pernah mengulang fase yang sudah selesai tanpa izin user.**
3. **Verifikasi fase aktif.** Sebelum mengerjakan tugas apa pun, nyatakan secara eksplisit ke user: "Saya melanjutkan dari [nama fase] — saya akan [tindakan berikutnya]." Tunggu konfirmasi singkat jika ada perubahan dari ekspektasi.
4. **Jangan asumsikan — verifikasi.** Jika `.workspaces/PROGRESS.md` tidak ada, buat terlebih dahulu sebelum melanjutkan.

## Standard Operating Procedure (SOP)

Urutan kerja wajib diikuti secara berurutan. Jangan loncat fase. **Patuhi Guardrails pada tiap fase dengan ketat!**

**ATURAN UMUM PROGRESS:** Setiap kali satu tugas atau fase selesai, agen **WAJIB seketika itu juga (real-time)** mencatatnya ke dalam `.workspaces/PROGRESS.md`. Jangan menunggu sampai akhir proyek.

---

### Fase 1: Setup & Environment (Manusia & Agen)

Clone repo ini, buat file `.env` dari `.env.example`, isi `SITE.md` & `DESIGN.md`.
*(Skill terkait: Gunakan **`wpsk-editorial-brainstorm`** jika butuh bantuan AI untuk merumuskan niche, branding, dan sistem desain dari nol; gunakan **`wp-wpcli-and-ops`** untuk task operasional server/database awal jika diperlukan).*

**GUARDRAILS SETUP:**

- Agen **WAJIB** membuat folder wajib `.workspaces/assets/` di awal inisialisasi sebagai tempat menyimpan gambar (logo), featured image, placeholder, dll yang akan diunggah ke website.
- Segera inisialisasi file `.workspaces/PROGRESS.md` menggunakan template dari `PROGRESS.example.md`.
- User **WAJIB** menyediakan file `.env` berisi `WP_USERNAME` dan `WP_APP_PASSWORD` (Application Password role Administrator).
- URL target diambil langsung dari field URL di `SITE.md`.
- Agen **WAJIB** memvalidasi koneksi ke WordPress REST API (`GET /wp-json/wp/v2/users/me`) menggunakan kredensial `.env` sebelum melangkah ke fase berikutnya.
- Agen **WAJIB** memverifikasi bahwa `DESIGN.md` terisi penuh — tidak ada field `{{ }}` yang tersisa.

---

### Fase 2: Perencanaan Arsitektur & PRD (@architect)

Sebelum proses pembuatan tema dimulai, agen `@architect` **WAJIB** menyusun dokumen PRD di `PRODUCT.md` (pastikan file ini terdaftar di `.gitignore`).
*(Skill terkait: Merujuk pada panduan art direction di **`frontend-design`** dan struktur hierarki template di **`wpsk-theme-convention`**).*

**GUARDRAILS PRD (`PRODUCT.md`):**

- Dokumen `PRODUCT.md` wajib memuat secara detail:
  1. **Daftar Template yang Akan Dibuat:** Seluruh template file yang direncanakan (`front-page.php`, `header.php`, `footer.php`, `single.php`, `page.php`, `archive.php`, `search.php`, `404.php`, dan komponen di `template-parts/`).
  2. **Struktur Wireframe & Layout:** Penjelasan hierarki blok dan komponen tata letak visual untuk setiap template, dengan fokus utama dan mendalam pada:
     - **Frontpage:** Hero headline grid, section artikel per kategori, trending block, sidebar layout, dan footer.
     - **Single Article:** Post header (judul, meta, kategori, author), featured media container, author bio box, breadcrumbs, konten Gutenberg layout, related posts grid, dan komentar/share box.
- **HARD GATE PRD:** Dokumen `PRODUCT.md` harus ditinjau dan disetujui oleh User sebelum `@engineer` mulai menulis kode tema. **Catat persetujuan ini di `.workspaces/PROGRESS.md`.**

---

### Fase 3: Pengembangan Tema (@engineer)

> **FASE INI HANYA BOLEH DIMULAI SETELAH:**
> 1. Baris "HARD GATE: PRD disetujui" sudah tertulis di `.workspaces/PROGRESS.md`
> 2. `DESIGN.md` dan `PRODUCT.md` sudah final dan lengkap

**INSTRUKSI PERTAMA @engineer:** Sebelum menulis kode apapun, **baca dulu** skill `wpsk-theme-convention` (`.agents/skills/wpsk-theme-convention/SKILL.md`) secara lengkap. Skill itu adalah spesifikasi teknis yang mengikat — bukan sekadar panduan.

**GUARDRAIL SKILLS (UI/UX):** Saat mulai merancang atau membangun UI tema, agen **WAJIB** membaca dan menerapkan instruksi dari empat skill berikut secara berurutan:

1. **`antislop-ui`** — filter utama anti-slop visual (komponen, kartu, bayangan, tombol).
2. **`antislop-human`** — aksesibilitas, kontras warna WCAG, dan navigasi keyboard.
3. **`antislop-layoutmobile`** — responsivitas, reflow grid, tap target 44px, dan anti-overflow.
4. **`frontend-design`** — art direction dan tipografi editorial yang distinctive.

*(Catatan Blok Kustom: Jika proyek memerlukan blok Gutenberg kustom khusus yang tidak dapat diakomodasi oleh tema atau core blocks, rujuk skill **`wp-block-development`**).*

**GUARDRAIL DESAIN & PRD:** `DESIGN.md` dan `PRODUCT.md` adalah **Sumber Kebenaran Mutlak**. Agen **DILARANG KERAS** mengubah spesifikasi tata letak atau token desain tanpa izin eksplisit dari user.

**GUARDRAIL TEMA (DINAMIS — TIDAK ADA PENGECUALIAN):**
- **DILARANG** hardcode HTML statis untuk navigasi → wajib `wp_nav_menu()`
- **DILARANG** hardcode `<img>` untuk logo → wajib `the_custom_logo()`
- **DILARANG** hardcode ID/slug artikel → wajib `WP_Query`
- **DILARANG** hardcode teks kategori → wajib `get_categories()`
- **DILARANG** gunakan Tailwind CDN → wajib build pipeline PostCSS lokal
- `functions.php` **wajib** mendeklarasikan `add_theme_support('custom-logo')`, `add_theme_support('post-thumbnails')`, dan `register_nav_menus()`

**GUARDRAIL BUILD & BUNDLING:**
- Semua coding tema dilakukan **secara lokal** di `.workspaces/theme-src/`.
- **JANGAN EDIT MANUAL** file `theme/style.css` atau `theme/js/` — ini adalah output build.
- Jalankan `npm run dev` setelah setiap batch perubahan untuk verifikasi.
- Output `.zip` dari `npm run bundle` **wajib** berada di root `.workspaces/`, **bukan** di dalam `theme-src/`.
- **SERAH TERIMA ZIP TEMA:** Hanya pada saat pembuatan tema selesai atau terjadi perubahan tema, agen **WAJIB** memberikan file ZIP tema yang ada di `.workspaces/` kepada user untuk diunggah/diperbarui.
- Screenshot 1200x900px dari Homepage disimpan sebagai `theme/screenshot.png` di dalam source tema.
- Agen **WAJIB** meng-generate file `.workspaces/THEME_SPECS.md` setelah bundling tema.

---

### Fase 4: Manajemen Penulis & Konten (@content)

**GUARDRAIL WP REST API:**
- Seluruh manajemen konten (pembuatan user, kategori, tag, halaman statis, dan artikel) **WAJIB** menggunakan **WordPress REST API** dengan autentikasi Application Password dari `.env`.
- Dilarang menggunakan WPVibe untuk pembuatan/pengunggahan konten teks dan data database.
- WPVibe MCP diizinkan **hanya untuk operasi yang tidak didukung REST API**, seperti mencari aset gambar via `search_images`.

**GUARDRAIL AUTHOR (MULTI-USER):**
- Sebelum menulis artikel apa pun, agen **WAJIB** membuat **3–5 user dengan role `author`** via REST API (`POST /wp-json/wp/v2/users`).
- Format email untuk setiap author **WAJIB**: `<username>@<site.com>` (Contoh: untuk domain `qloov.com` dengan username `rodi`, emailnya adalah `rodi@qloov.com`).
- **DILARANG KERAS** mempublikasikan artikel menggunakan akun `admin`. Seluruh artikel wajib diatribusikan ke salah satu dari author yang telah dibuat sebelumnya secara bergantian (rotasi merata).

**GUARDRAIL PENULISAN PARALEL VIA SUBAGENTS:**
- Proses penulisan artikel **WAJIB dilakukan secara paralel melalui subagents**.
- Agen utama mendefinisikan/memanggil beberapa subagent `@content` sekaligus, masing-masing bertugas menuntaskan satu artikel lengkap:
  - Merujuk pada panduan skill **`wpsk-seo-writer`** untuk standar editorial tinggi, anti-slop bahasa Indonesia, zero fluff, dan optimasi GEO/AEO.
  - Memformat isi artikel menggunakan sintaks *Gutenberg Blocks* murni merujuk pada skill **`wp-patterns`**. Dilarang menggunakan classic block/HTML mentah.
  - Menyiapkan *Featured Image* (dapat menggunakan WPVibe `search_images` untuk mencari referensi visual), mengunggahnya ke Media Library via REST API, dan menetapkannya sebagai post thumbnail.
  - Mengunggah dan mempublikasikan artikel via REST API dengan `author` ID dari salah satu user author yang telah dibuat.

---

### Fase 5: QA (@qa)

Audit menyeluruh sebelum promosi situs:
- **Performa Backend:** Menggunakan skill **`wp-performance`** untuk profiling query SQL berat, pembersihan autoload options, dan evaluasi cache database.
- **Aksesibilitas & Kontras:** Menggunakan skill **`antislop-human`** untuk validasi kontras warna teks (WCAG AA/AAA min 4.5:1) dan navigasi keyboard (`focus-visible`).
- **Audit Responsivitas Layar:** Menggunakan skill **`antislop-layoutmobile`** untuk memastikan tidak ada horizontal overflow di viewport 375px, 768px, 1280px dan tap target >= 44px.
- **Audit SEO & Links:** Lighthouse SEO & Performa >= 80, validasi broken links, serta ketersediaan XML Sitemap.

---

### Fase 6: Deployment & Serah Terima (Manusia)

Manusia mengunggah file ZIP tema terbaru dari `.workspaces/` ke `wp-admin → Appearance → Themes → Add New → Upload Theme`, mengaktifkannya, dan memvalidasi tampilan akhir website secara langsung bersama seluruh konten yang telah diinjeksi.
*(Skill terkait: Gunakan **`wp-wpcli-and-ops`** jika operator memerlukan search-replace database atau flush cache server pasca-deploy).*

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
- **DILARANG** membuat file baru di luar `.workspaces/` kecuali untuk mengupdate template inti (`AGENTS.md`, `README.md`, `.gitignore`, `.env.example`, atau file example) serta skill di `.agents/skills/`.

## Conventions

Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `PRODUCT.md` dan `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.

**Aturan Pembuatan Skill Baru:** Jika agen atau manusia membuat custom skill spesifik untuk ekosistem *Starter Kit* ini, nama folder dan `name:` di YAML *wajib* menggunakan awalan `wpsk-` (WordPress Starter Kit). Contoh: `wpsk-editorial-brainstorm`, `wpsk-theme-convention`, `wpsk-seo-writer`.

## Matriks Penugasan Skill per Fase Kerja

| Fase Proyek | Peran Agen | Skill Kunci yang Ditugaskan |
| :--- | :--- | :--- |
| **Fase 1: Setup & Env** | `@architect` / User | `wpsk-editorial-brainstorm`, `wp-wpcli-and-ops` |
| **Fase 2: Arsitektur & PRD** | `@architect` | `frontend-design`, `wpsk-theme-convention` |
| **Fase 3: Tema** | `@engineer` | `wpsk-theme-convention`, `antislop-ui`, `antislop-human`, `antislop-layoutmobile`, `frontend-design`, `wp-block-development` *(opsional)* |
| **Fase 4: Penulis & Konten** | `@content` (Paralel Subagents) | `wpsk-seo-writer`, `wp-patterns` |
| **Fase 5: QA** | `@qa` | `wp-performance`, `antislop-human`, `antislop-layoutmobile` |
| **Fase 6: Deployment & Ops** | Manusia & Agen | `wp-wpcli-and-ops` |
| **Meta Tooling** | Agen & Manusia | `skill-creator` |

## Boundaries (Jangan Lakukan)

- Jangan ubah wp-login atau pengaturan inti wp-admin tanpa persetujuan eksplisit.
- Jangan gunakan FSE block theme penuh atau page builder berat (Elementor/Divi) sebagai basis tema.
- Jangan hardcode kredensial WordPress di dalam file atau skrip; selalu baca `WP_USERNAME` dan `WP_APP_PASSWORD` dari file `.env`.
- Jangan operasikan situs WordPress mana pun selain yang tercantum di field URL `SITE.md`.
- Dilarang membuat artikel atas nama user admin. Selalu gunakan user author yang telah dibuat.
- Dilarang menggunakan WPVibe untuk manajemen konten utama (gunakan WP REST API). WPVibe hanya untuk operasi di luar REST API (seperti pencarian gambar).
- Dilarang menulis artikel secara sekuensial jika dapat dijalankan secara paralel via subagent.
- Dilarang memulai koding tema sebelum dokumen `PRODUCT.md` dibuat dan disetujui user.
- Jangan gunakan Tailwind CDN untuk tema. Build pipeline PostCSS adalah satu-satunya cara.

## Definition of Done

PRD `PRODUCT.md` disetujui, tema kustom dinamis & responsif selesai dan di-bundle ke ZIP root `.workspaces/`, 3–5 user author terdaftar, kategori & halaman statis terisi via REST API, minimal artikel SEO Gutenberg terbit paralel dengan featured image dan author terdistribusi, Lighthouse >=80, file `.workspaces/THEME_SPECS.md` digenerate.

## Changelog

Catat setiap pekerjaan yang selesai di repo ini. Entri terbaru di atas.

### `06. 2026-09-10`

- **Pemetaan Eksplisit Skill ke Task:** Menambahkan matriks penugasan skill per fase kerja dan mereferensikan secara spesifik setiap skill aktif (`wpsk-*`, `antislop-*`, `wp-*`) pada setiap task SOP di `AGENTS.md` dan `PROGRESS.example.md`.
- **Pembersihan Skill Irrelevan:** Menghapus 9 skill plugin/API WordPress yang tidak sesuai arsitektur dan 3 skill antislop redundan, mempertahankan 12 skill paling esensial.

### `05. 2026-09-10`

- **Pembuatan Skill `wpsk-seo-writer`:** Mengelaborasi keunggulan `indo-seo-writer` dengan arsitektur `seo-article` dalam bahasa Inggris di `.agents/skills/wpsk-seo-writer/`.

### `04. 2026-09-10`

- **Integrasi WP REST API & .env:** Mengalihkan manajemen konten ke WP REST API via Application Password.
- **PRD di PRODUCT.md & Multi-Author:** Wajib PRD sebelum koding tema, serta pembuatan 3-5 author `<username>@<site.com>`.

### `03. 2026-09-08`

- Sinkronisasi dokumen tema dan integrasi skill UI.
