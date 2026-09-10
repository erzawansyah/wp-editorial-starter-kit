# AGENTS.md

## Project Overview

Repo ini adalah **Starter Kit** untuk produksi massal website niche blog/editorial berbasis WordPress. Setiap proyek baru dimulai dengan meng-clone repo ini, mengisi `SITE.md` dan `DESIGN.md`, lalu menjalankan workflow di bawah. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun.
Repo ini adalah **Starter Kit** untuk produksi massal website niche blog/editorial berbasis WordPress. Setiap proyek baru dimulai dengan meng-clone repo ini, mengisi `.env`, `SITE.md`, dan `DESIGN.md`, lalu menjalankan workflow di bawah. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun.

Struktur baku setiap website yang dihasilkan: header menu kategori, homepage hero grid + block per kategori + trending, sidebar opsional, footer latest article, halaman statis, single post/page, archive kategori, search, 404.

## Tech Stack

WordPress (PHP 8.2+), classic theme + Tailwind CSS. Koneksi AI ke situs via WPVibe MCP. AI client: Antigravity.
WordPress (PHP 8.2+), classic theme + Tailwind CSS. Manajemen konten via WordPress REST API (Basic Auth Application Password dari `.env`). WPVibe MCP digunakan khusus untuk operasi di luar REST API (seperti pencarian gambar/featured image). AI client: Antigravity.

## Agents

- **@architect** - baca SITE.md & DESIGN.md, susun rencana struktur & wireframe. Tidak menulis kode.
- **@content** - generate kategori, halaman statis, logo/favicon, draft artikel awal.
- **@engineer** - bangun tema classic + Tailwind secara lokal di dalam folder workspaces (tanpa WPVibe).
- **@architect** - baca `SITE.md` & `DESIGN.md`, susun PRD di `PRODUCT.md` (daftar template & wireframe mendalam terutama frontpage dan single artikel). Tidak menulis kode tema.
- **@engineer** - bangun tema classic + Tailwind secara lokal di `.workspaces/theme-src/` mengacu pada `PRODUCT.md` dan `DESIGN.md`. Menyerahkan bundle ZIP tema di root `.workspaces/` setiap ada perubahan tema.
- **@content** - kelola konten via WP REST API: buat 3–5 user author, taksonomi, halaman statis, serta memimpin penulisan artikel SEO Gutenberg secara paralel melalui subagent.
- **@content** - kelola konten via WP REST API: buat 3–5 user author, taksonomi, halaman statis, serta memimpin penulisan artikel SEO Gutenberg secara paralel melalui subagent (menggunakan skill `wpsk-seo-writer`).
- **@qa** - audit Lighthouse, broken link, responsivitas sebelum promosi ke produksi.

## Sesi Lintas Session — Cara Melanjutkan Pekerjaan

> **WAJIB DIBACA DI AWAL SETIAP SESI BARU:**

1. **Baca SITE.md.** Jika ada field `{{ }}` yang belum terisi, **BERHENTI** dan tanyakan ke user sebelum melakukan apapun.
1. **Baca SITE.md dan .env.** Jika ada field `{{ }}` di `SITE.md` atau kredensial di `.env` belum terisi, **BERHENTI** dan tanyakan ke user sebelum melakukan apapun.
2. **Baca `.workspaces/PROGRESS.md`.** Dokumen ini adalah satu-satunya sumber kebenaran tentang posisi proyek saat ini. Identifikasi fase terakhir yang selesai dan lanjutkan dari sana. **Jangan pernah mengulang fase yang sudah selesai tanpa izin user.**
3. **Verifikasi fase aktif.** Sebelum mengerjakan tugas apa pun, nyatakan secara eksplisit ke user: "Saya melanjutkan dari [nama fase] — saya akan [tindakan berikutnya]." Tunggu konfirmasi singkat jika ada perubahan dari ekspektasi.
4. **Jangan asumsikan — verifikasi.** Jika `.workspaces/PROGRESS.md` tidak ada, buat terlebih dahulu sebelum melanjutkan.

## Standard Operating Procedure (SOP)

Urutan kerja wajib diikuti secara berurutan. Jangan loncat fase. **Patuhi Guardrails pada tiap fase dengan ketat!**

**ATURAN UMUM PROGRESS:** Setiap kali satu tugas atau fase selesai, agen **WAJIB seketika itu juga (real-time)** mencatatnya ke dalam `.workspaces/PROGRESS.md`. Jangan menunggu sampai akhir proyek.

---

### Fase 1: Setup (Manusia & Agen)
### Fase 1: Setup & Environment (Manusia & Agen)

Clone repo ini, isi `SITE.md` & `DESIGN.md`. *(Catatan: Panggil skill `wpsk-editorial-brainstorm` jika butuh bantuan AI untuk merumuskan niche, branding, dan sistem desain dari nol).*
Clone repo ini, buat file `.env` dari `.env.example`, isi `SITE.md` & `DESIGN.md`. *(Catatan: Panggil skill `wpsk-editorial-brainstorm` jika butuh bantuan AI untuk merumuskan niche, branding, dan sistem desain dari nol).*

**GUARDRAILS SETUP:**

- Agen **WAJIB** membuat folder wajib `.workspaces/assets/` di awal inisialisasi sebagai tempat menyimpan gambar (logo), featured image, placeholder, dll yang akan diunggah ke website.
- Segera inisialisasi file `.workspaces/PROGRESS.md` menggunakan template dari `PROGRESS.example.md`.
- Agen **WAJIB** menjalankan `wp rewrite structure '/%postname%/'` (via WPVibe) untuk menghapus `index.php`.
- Agen **WAJIB** menginstal dan mengaktifkan tema **GeneratePress** (`wp theme install generatepress --activate`) di awal proyek. Tema ini digunakan sebagai kanvas netral untuk memvalidasi kesiapan konten.
- User **WAJIB** menyediakan file `.env` berisi `WP_USERNAME` dan `WP_APP_PASSWORD` (Application Password role Administrator).
- URL target diambil langsung dari field URL di `SITE.md`.
- Agen **WAJIB** memvalidasi koneksi ke WordPress REST API (`GET /wp-json/wp/v2/users/me`) menggunakan kredensial `.env` sebelum melangkah ke fase berikutnya.
- Agen **WAJIB** memverifikasi bahwa `DESIGN.md` terisi penuh — tidak ada field `{{ }}` yang tersisa.

---

### Fase 2: Konten (@content)
### Fase 2: Perencanaan Arsitektur & PRD (@architect)

**GUARDRAIL PENULISAN (SEO):** Saat membuat draf artikel atau *copywriting* halaman statis, agen **WAJIB** merujuk pada instruksi dari skill `seo-article` untuk memastikan tulisan memiliki standar SEO yang tinggi, kaya akan data riset, dan tidak terdengar seperti konten AI generik (*slop*).
Sebelum proses pembuatan tema dimulai, agen `@architect` **WAJIB** menyusun dokumen PRD di `PRODUCT.md` (pastikan file ini terdaftar di `.gitignore`).

**GUARDRAIL KONTEN:** **DILARANG KERAS** membuat konten *dummy* hanya dalam bentuk file lokal/teks. Agen **WAJIB** menggunakan WPVibe MCP (REST API atau WP-CLI) untuk menginjeksi artikel SEO final, halaman statis (Tentang Kami, dll), dan struktur kategori **langsung** ke database server remote.
**GUARDRAILS PRD (`PRODUCT.md`):**

**GUARDRAIL FORMAT (GUTENBERG & MEDIA):** Seluruh artikel dan halaman yang diunggah **WAJIB** diformat menggunakan struktur sintaks *Gutenberg Blocks* murni (agen dapat merujuk pada panduan sintaksis blok di dalam skill `wp-patterns`), **DILARANG KERAS** menggunakan HTML mentah (*classic block*). Selain itu, agen **WAJIB** meng-generate *Featured Image* dan menetapkannya (set *post thumbnail*) untuk setiap artikel yang dipublikasikan.
- Dokumen `PRODUCT.md` wajib memuat secara detail:
  1. **Daftar Template yang Akan Dibuat:** Seluruh template file yang direncanakan (`front-page.php`, `header.php`, `footer.php`, `single.php`, `page.php`, `archive.php`, `search.php`, `404.php`, dan komponen di `template-parts/`).
  2. **Struktur Wireframe & Layout:** Penjelasan hierarki blok dan komponen tata letak visual untuk setiap template, dengan fokus utama dan mendalam pada:
     - **Frontpage:** Hero headline grid, section artikel per kategori, trending block, sidebar layout, dan footer.
     - **Single Article:** Post header (judul, meta, kategori, author), featured media container, author bio box, breadcrumbs, konten Gutenberg layout, related posts grid, dan komentar/share box.
- **HARD GATE PRD:** Dokumen `PRODUCT.md` harus ditinjau dan disetujui oleh User sebelum `@engineer` mulai menulis kode tema. **Catat persetujuan ini di `.workspaces/PROGRESS.md`.**

**HARD GATE (VALIDASI KONTEN):** Setelah semua artikel, kategori, tag, halaman statis, dan navigasi menu selesai diunggah, minta Manusia (User) untuk meninjau website secara visual. Karena tema yang aktif adalah GeneratePress, Manusia bisa dengan mudah memastikan seluruh struktur data (konten) sudah benar-benar siap dan masuk ke database. Pengembangan tema kustom **DILARANG** dimulai sebelum ada persetujuan "Konten Siap" dari Manusia. **Catat persetujuan ini di `.workspaces/PROGRESS.md`.**

---

### Fase 3: Tema (@architect → @engineer)
### Fase 3: Pengembangan Tema (@engineer)

> **FASE INI HANYA BOLEH DIMULAI SETELAH:**
> 1. Baris "HARD GATE: Konten disetujui" sudah tertulis di `.workspaces/PROGRESS.md`
> 2. `DESIGN.md` tidak memiliki field `{{ }}` yang tersisa
> 1. Baris "HARD GATE: PRD disetujui" sudah tertulis di `.workspaces/PROGRESS.md`
> 2. `DESIGN.md` dan `PRODUCT.md` sudah final dan lengkap

**INSTRUKSI PERTAMA @engineer:** Sebelum menulis kode apapun, **baca dulu** skill `wpsk-theme-convention` (`.agents/skills/wpsk-theme-convention/SKILL.md`) secara lengkap. Skill itu adalah spesifikasi teknis yang mengikat — bukan sekadar panduan.

**GUARDRAIL SKILLS (UI/UX):** Saat mulai merancang atau membangun UI tema, agen **WAJIB** membaca dan menerapkan instruksi dari tiga skill berikut secara berurutan:
**GUARDRAIL SKILLS (UI/UX):** Saat mulai merancang atau membangun UI tema, agen **WAJIB** membaca dan menerapkan instruksi dari empat skill berikut secara berurutan:

1. `antislop-ui` — filter utama anti-slop visual
2. `antislop-human` — aksesibilitas dan kontras warna
3. `antislop-layoutmobile` — responsivitas dan layout mobile
4. `frontend-design` — art direction dan tipografi editorial yang distinctive

**GUARDRAIL DESAIN (STRICT DESIGN.md):** `DESIGN.md` adalah **Sumber Kebenaran Mutlak (Single Source of Truth)**. Agen **DILARANG KERAS** mengubah isi dokumen `DESIGN.md` yang sudah ditentukan tanpa izin eksplisit dari user. Seluruh implementasi harus tunduk pada spesifikasi di dalam dokumen tersebut.
**GUARDRAIL DESAIN & PRD:** `DESIGN.md` dan `PRODUCT.md` adalah **Sumber Kebenaran Mutlak**. Agen **DILARANG KERAS** mengubah spesifikasi tata letak atau token desain tanpa izin eksplisit dari user.

**GUARDRAIL TEMA (DINAMIS — TIDAK ADA PENGECUALIAN):**
- **DILARANG** hardcode HTML statis untuk navigasi → wajib `wp_nav_menu()`
- **DILARANG** hardcode `<img>` untuk logo → wajib `the_custom_logo()`
- **DILARANG** hardcode ID/slug artikel → wajib `WP_Query`
- **DILARANG** hardcode teks kategori → wajib `get_categories()`
- **DILARANG** gunakan Tailwind CDN → wajib build pipeline PostCSS lokal
- `functions.php` **wajib** mendeklarasikan `add_theme_support('custom-logo')` dan `register_nav_menus()`
- `functions.php` **wajib** mendeklarasikan `add_theme_support('custom-logo')`, `add_theme_support('post-thumbnails')`, dan `register_nav_menus()`

**GUARDRAIL BUILD:**
- Semua coding tema dilakukan **secara lokal** di `.workspaces/theme-src/`
- **DILARANG** menggunakan WPVibe untuk menulis atau mengedit file PHP/CSS/JS tema
- **JANGAN EDIT MANUAL** file `theme/style.css` atau `theme/js/` — ini adalah output build
- Jalankan `npm run dev` setelah setiap batch perubahan untuk verifikasi
**GUARDRAIL BUILD & BUNDLING:**
- Semua coding tema dilakukan **secara lokal** di `.workspaces/theme-src/`.
- **JANGAN EDIT MANUAL** file `theme/style.css` atau `theme/js/` — ini adalah output build.
- Jalankan `npm run dev` setelah setiap batch perubahan untuk verifikasi.
- Output `.zip` dari `npm run bundle` **wajib** berada di root `.workspaces/`, **bukan** di dalam `theme-src/`.
- **SERAH TERIMA ZIP TEMA:** Hanya pada saat pembuatan tema selesai atau terjadi perubahan tema, agen **WAJIB** memberikan file ZIP tema yang ada di `.workspaces/` kepada user untuk diunggah/diperbarui.
- Screenshot 1200x900px dari Homepage disimpan sebagai `theme/screenshot.png` di dalam source tema.
- Agen **WAJIB** meng-generate file `.workspaces/THEME_SPECS.md` setelah bundling tema.

**GUARDRAIL SCREENSHOT:** Setelah tema *final*, agen atau manusia **WAJIB** membuat screenshot berukuran 1200x900px dari Homepage dan menyimpannya sebagai `theme/screenshot.png` di dalam source tema.
---

**GUARDRAIL BUNDLING:** Output `.zip` dari `npm run bundle` **wajib** berada di root `.workspaces/`, **bukan** di dalam `theme-src/`. Pastikan `package.json` dikonfigurasi untuk ini.
### Fase 4: Manajemen Penulis & Konten (@content)

**GUARDRAIL HANDOVER:** Setelah tema selesai dan di-bundle, agen **WAJIB** meng-generate file `.workspaces/THEME_SPECS.md` yang berisi spesifikasi arsitektur teknis tema sebagai dokumen referensi mutlak untuk sesi AI di masa depan.
**GUARDRAIL WP REST API:**
- Seluruh manajemen konten (pembuatan user, kategori, tag, halaman statis, dan artikel) **WAJIB** menggunakan **WordPress REST API** dengan autentikasi Application Password dari `.env`.
- Dilarang menggunakan WPVibe untuk pembuatan/pengunggahan konten teks dan data database.
- WPVibe MCP diizinkan **hanya untuk operasi yang tidak didukung REST API**, seperti mencari aset gambar via `search_images`.

**CHECKLIST WAJIB SEBELUM BUNDLE:** Jalankan seluruh checklist di `wpsk-theme-convention/SKILL.md` bagian "Checklist Fase Tema". Semua item harus ✅ sebelum `npm run bundle` dijalankan.
**GUARDRAIL AUTHOR (MULTI-USER):**
- Sebelum menulis artikel apa pun, agen **WAJIB** membuat **3–5 user dengan role `author`** via REST API (`POST /wp-json/wp/v2/users`).
- Format email untuk setiap author **WAJIB**: `<username>@<site.com>` (Contoh: untuk domain `qloov.com` dengan username `rodi`, emailnya adalah `rodi@qloov.com`).
- **DILARANG KERAS** mempublikasikan artikel menggunakan akun `admin`. Seluruh artikel wajib diatribusikan ke salah satu dari author yang telah dibuat sebelumnya secara bergantian (rotasi merata).

**GUARDRAIL PENULISAN PARALEL VIA SUBAGENTS:**
- Proses penulisan artikel **WAJIB dilakukan secara paralel melalui subagents**.
- Agen utama mendefinisikan/memanggil beberapa subagent `@content` sekaligus, masing-masing bertugas menuntaskan satu artikel lengkap:
  - Merujuk pada panduan skill `seo-article` untuk standar editorial tinggi.
  - Merujuk pada panduan skill `wpsk-seo-writer` untuk standar editorial tinggi, anti-slop bahasa Indonesia, zero fluff, dan optimasi GEO/AEO.
  - Memformat isi artikel menggunakan sintaks *Gutenberg Blocks* murni (`wp-patterns`). Dilarang menggunakan classic block/HTML mentah.
  - Menyiapkan *Featured Image* (dapat menggunakan WPVibe `search_images` untuk mencari referensi visual), mengunggahnya ke Media Library via REST API, dan menetapkannya sebagai post thumbnail.
  - Mengunggah dan mempublikasikan artikel via REST API dengan `author` ID dari salah satu user author yang telah dibuat.

---

### Fase 4: QA (@qa)
### Fase 5: QA (@qa)

Audit Lighthouse >=80 (performa & SEO), broken link check, uji responsivitas di mobile (375px), tablet (768px), desktop (1280px).

---

### Fase 5: Deployment (Manusia)
### Fase 6: Deployment & Serah Terima (Manusia)

Karena zip sudah dipisahkan ke luar root source tema, Manusia bisa langsung mengunggah file ZIP tersebut secara manual ke `wp-admin → Appearance → Themes → Add New → Upload Theme`. Tidak perlu paksakan upload via API/agen jika tidak stabil.
Manusia mengunggah file ZIP tema terbaru dari `.workspaces/` ke `wp-admin → Appearance → Themes → Add New → Upload Theme`, mengaktifkannya, dan memvalidasi tampilan akhir website secara langsung bersama seluruh konten yang telah diinjeksi.

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
- **DILARANG** membuat file baru di luar `.workspaces/` kecuali untuk mengupdate template inti (`AGENTS.md`, `README.md`, `.gitignore`, `.env.example`, atau file example).
- **DILARANG** membuat file baru di luar `.workspaces/` kecuali untuk mengupdate template inti (`AGENTS.md`, `README.md`, `.gitignore`, `.env.example`, atau file example) serta skill di `.agents/skills/`.

## Conventions

Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.
Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `PRODUCT.md` dan `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.

**Aturan Pembuatan Skill Baru:** Jika agen atau manusia membuat custom skill spesifik untuk ekosistem *Starter Kit* ini, nama folder dan `name:` di YAML *wajib* menggunakan awalan `wpsk-` (WordPress Starter Kit). Contoh: `wpsk-editorial-brainstorm`, `wpsk-theme-convention`.
**Aturan Pembuatan Skill Baru:** Jika agen atau manusia membuat custom skill spesifik untuk ekosistem *Starter Kit* ini, nama folder dan `name:` di YAML *wajib* menggunakan awalan `wpsk-` (WordPress Starter Kit). Contoh: `wpsk-editorial-brainstorm`, `wpsk-theme-convention`, `wpsk-seo-writer`.

## Skill UI yang Aktif (Fase Tema)

Daftar skill UI yang **wajib digunakan** di fase tema, berurutan sesuai prioritas. Tidak ada skill lain di luar daftar ini yang diizinkan untuk UI work:
Daftar skill UI yang **wajib digunakan** di fase tema, berurutan sesuai prioritas:

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
- Jangan hardcode kredensial WordPress di dalam file atau skrip; selalu baca `WP_USERNAME` dan `WP_APP_PASSWORD` dari file `.env`.
- Jangan operasikan situs WordPress mana pun selain yang tercantum di field URL `SITE.md`.
- WordPress berada di server remote. Seluruh interaksi ke WordPress **wajib** dilakukan melalui WPVibe MCP — kecuali penulisan kode tema (lokal).
- Jangan mulai Fase Tema sebelum `.workspaces/PROGRESS.md` mencatat persetujuan Hard-Gate Konten dari user.
- Dilarang membuat artikel atas nama user admin. Selalu gunakan user author yang telah dibuat.
- Dilarang menggunakan WPVibe untuk manajemen konten utama (gunakan WP REST API). WPVibe hanya untuk operasi di luar REST API (seperti pencarian gambar).
- Dilarang menulis artikel secara sekuensial jika dapat dijalankan secara paralel via subagent.
- Dilarang memulai koding tema sebelum dokumen `PRODUCT.md` dibuat dan disetujui user.
- Jangan gunakan Tailwind CDN untuk tema. Build pipeline PostCSS adalah satu-satunya cara.

## Definition of Done

Kategori & halaman statis terisi (via DB), draft tema disetujui (dinamis & responsif), Lighthouse >=80, permalink beres, file zip terpisah di root `.workspaces/`, THEME_SPECS.md ter-generate, screenshot.png tersedia, backup pra-publish terverifikasi.
PRD `PRODUCT.md` disetujui, tema kustom dinamis & responsif selesai dan di-bundle ke ZIP root `.workspaces/`, 3–5 user author terdaftar, kategori & halaman statis terisi via REST API, minimal artikel SEO Gutenberg terbit paralel dengan featured image dan author terdistribusi, Lighthouse >=80, file `.workspaces/THEME_SPECS.md` digenerate.

## Changelog

Catat setiap pekerjaan yang selesai di repo ini. Entri terbaru di atas.

### `05. 2026-09-10`

- **Pembuatan Skill `wpsk-seo-writer`:** Mengelaborasi keunggulan `indo-seo-writer` (anti-slop bahasa Indonesia, zero basa-basi, single-topic heading tanpa kata "dan", tanpa contrastive negation, tanpa em-dash, panjang fleksibel 600-800 atau >1300 kata) dengan arsitektur `seo-article` (Definition Engineering GEO formula, question-format H2 PAA, tabel perbandingan berpresisi tinggi, dan meta output block). Ditulis dalam bahasa Inggris di `.agents/skills/wpsk-seo-writer/`.

### `04. 2026-09-10`

- **Integrasi WP REST API & .env:** Mengalihkan seluruh manajemen konten (user, taksonomi, halaman, post) ke WordPress REST API murni menggunakan kredensial Application Password dari `.env`.
- **WPVibe Scoped:** Membatasi peran WPVibe MCP hanya untuk kebutuhan spesifik yang tidak didukung REST API (misal: pencarian referensi gambar `search_images`).
- **PRD di PRODUCT.md:** Menambahkan Fase 2 khusus arsitektur PRD oleh `@architect` yang menghasilkan `PRODUCT.md` (daftar template & wireframe detail frontpage + single) sebelum coding tema dimulai.
- **Multi-Author Mandatory:** Mewajibkan pembuatan 3–5 akun user `author` via REST API dengan email `<username>@<site.com>`, dan melarang penerbitan artikel menggunakan akun admin.
- **Subagent Parallel Content:** Mewajibkan proses pembuatan draf dan publikasi artikel dieksekusi secara paralel menggunakan subagents.
- **On-Demand Theme ZIP Handover:** File ZIP tema diserahkan kepada user setiap kali selesai pembuatan atau perubahan tema.

### `03. 2026-09-08`

- **Sinkronisasi Dokumen:** Rewrite total `wpsk-theme-convention/SKILL.md` agar selaras 100% dengan `AGENTS.md` — menghapus instruksi WPVibe yang kontradiktif, menambahkan prasyarat Hard-Gate dan DESIGN.md check, memperjelas arsitektur source vs output, menambahkan aturan elemen dinamis eksplisit dengan kode contoh, dan checklist wajib sebelum bundling.
- **Efisiensi Skill UI:** Menghapus 5 skill UI yang tidak relevan atau tumpang tindih (`baseline-ui`, `web-design-guidelines`, `wpds`, `ui-ux-pro-max`, `impeccable`). Hanya menyisakan 4 skill UI terintegrasi: `antislop-ui`, `antislop-human`, `antislop-layoutmobile`, `frontend-design`.
- **Enforcement Lintas Sesi:** Menambahkan seksi "Sesi Lintas Session" di `AGENTS.md` yang mewajibkan agen membaca `PROGRESS.md` terlebih dahulu sebelum bekerja, mencegah pengulangan fase dan inkonsistensi antar sesi.
- **Guardrail Tema yang Diperkuat:** Memperjelas setiap guardrail fase tema dengan perintah spesifik (dinamis vs hardcode, build pipeline, lokasi output zip, urutan baca skill).
- **Sinkronisasi Dokumen:** Rewrite total `wpsk-theme-convention/SKILL.md` agar selaras 100% dengan `AGENTS.md`.
- **Efisiensi Skill UI:** Menyisakan 4 skill UI terintegrasi: `antislop-ui`, `antislop-human`, `antislop-layoutmobile`, `frontend-design`.
- **Enforcement Lintas Sesi:** Menambahkan seksi "Sesi Lintas Session" di `AGENTS.md` yang mewajibkan agen membaca `PROGRESS.md`.

### `02. 2026-09-05`

- **Generic Rebranding:** Menghapus seluruh referensi spesifik "Croco" untuk menjadikannya *starter kit* netral.
- **Strict Local Theme:** Menegaskan pengembangan tema secara luring di folder `.workspaces/theme-src/` tanpa memodifikasi *live site* via WPVibe.
- **Workspace Architecture:** Merapikan dan meratakan (*flatten*) struktur folder `.workspaces/` dengan sub-direktori spesifik (`/temp`, `/scripts`, `/assets`) untuk mencegah penumpukan file.
- **Content Guardrails:** Mewajibkan penggunaan skill `seo-article` untuk standar SEO, serta `wp-patterns` untuk memastikan seluruh unggahan artikel menggunakan sintaks murni *Gutenberg Blocks* berikut *Featured Image*.
- **Strict Local Theme:** Menegaskan pengembangan tema secara luring di folder `.workspaces/theme-src/`.
- **Workspace Architecture:** Merapikan struktur folder `.workspaces/`.

### `01. 2026-09-03`

- Integrasi aturan Real-time Progress Tracking, Workspace Assets, Strict Dynamic Element, Auto-rename Theme, Hard-Gate Content Validation (GeneratePress), dan THEME_SPECS.md Handover Document.
- Inisialisasi awal Starter Kit.
