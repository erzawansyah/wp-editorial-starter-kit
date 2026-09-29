# AGENTS.md

## Project Overview

Repo ini adalah **Starter Kit** untuk produksi massal website niche blog/editorial berbasis WordPress. Setiap proyek baru dimulai dengan meng-clone repo ini, mengisi `.env`, `SITE.md`, dan `DESIGN.md`, lalu menjalankan workflow di bawah. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun.

Struktur baku setiap website yang dihasilkan: header menu kategori dengan container logo adaptif, homepage hero grid + variasi block per kategori + trending list + pagination ke archive, custom sidebar, footer latest article, halaman statis, single post (dengan tombol bagikan social share 6 kanal, author box, comment box ter-styling, dan custom sidebar), author archive page (`author.php`), category archive, search, 404.

## Tech Stack

WordPress (PHP 8.2+), classic theme + Tailwind CSS. Manajemen konten via WordPress REST API (Basic Auth Application Password dari `.env`) dan Easy MCP AI. Pexafy MCP digunakan untuk pencarian gambar/featured image editorial berkualitas tinggi. AI client: Antigravity.

## Modular Rules Reference

Untuk kepatuhan teknis mendalam dan efisiensi context window, guardrails detail didelegasikan ke rules modular di `.agents/rules/`:
- **[theme-guardrails.md](file:///.agents/rules/theme-guardrails.md)**: 8 aturan baku arsitektur tema WordPress, logo anti-meluap, dynamic frontpage section, `single.php`, `author.php`, `page.php`, dan build pipeline.
- **[cyberpanel-safety.md](file:///.agents/rules/cyberpanel-safety.md)**: Keamanan API Access, larangan mutasi server global tanpa izin, dan konfirmasi deploy otomatis.
- **[content-integrity.md](file:///.agents/rules/content-integrity.md)**: Diversitas author multi-etnis Indonesia, larangan akun admin, verifikasi fakta riset, dan format Gutenberg.

## Agents

- **@architect** - baca `SITE.md` & `DESIGN.md`, susun PRD di `PRODUCT.md` (daftar template & wireframe mendalam: variasi layout section per kategori, container logo aman, single post dengan tombol share & author box, custom sidebar, pagination frontpage, dan author archive). Mengacu pada `wpsk-theme-craft` (perintah `shape`) dan `wpsk-theme-convention`. Tidak menulis kode tema.
- **@content** - eksekusi **Content-First**: buat 3–5 user author dengan nama beragam (anti-Dimas/Pramesti), taksonomi (kategori & tag), halaman statis, serta daftarkan struktur Menu Header & Footer di WordPress via REST API sebelum tema dibangun. Memimpin penulisan artikel SEO Gutenberg secara paralel melalui subagent (menggunakan skill `wpsk-seo-writer` dan `wp-patterns`).
- **@engineer** - bangun tema classic + Tailwind secara lokal di `.workspaces/theme-src/` mengacu pada data konten yang sudah ada, `PRODUCT.md`, `DESIGN.md`, `wpsk-theme-convention`, standar visual `wpsk-theme-craft`, dan `.agents/rules/theme-guardrails.md`. Menyerahkan bundle ZIP tema di root `.workspaces/` setiap ada perubahan tema.
- **@qa** - audit Lighthouse, performa backend (`wp-performance`), audit a11y & mobile reflow (`wpsk-theme-craft` perintah `audit` & kalkulator kontras Python), serta mengambil **Full-Page Screenshot Desktop (1440px) dan Mobile (375px) via Playwright** untuk disematkan di Artifact sebelum promosi ke produksi.

## Sesi Lintas Session — Cara Melanjutkan Pekerjaan

> **WAJIB DIBACA DI AWAL SETIAP SESI BARU:**

1. **Baca SITE.md dan .env.** Jika ada field `{{ }}` di `SITE.md` atau kredensial di `.env` belum terisi, **BERHENTI** dan tanyakan ke user sebelum melakukan apapun.
2. **Baca `.workspaces/PROGRESS.md`.** Dokumen ini adalah satu-satunya sumber kebenaran tentang posisi proyek saat ini. Identifikasi fase terakhir yang selesai dan lanjutkan dari sana. **Jangan pernah mengulang fase yang sudah selesai tanpa izin user.**
3. **Cek Versi Template (Hemat Token):** Bandingkan angka `template_version` di `version.json` dengan `**Template Version:**` di header `.workspaces/PROGRESS.md`.
   - **Jika SAMA:** DILARANG membaca `UPDATE.md` (hemat token). Langsung lanjutkan ke langkah berikutnya.
   - **Jika BERBEDA (atau belum ada):** Baca bagian versi terkait di `UPDATE.md`, ingatkan pengguna jika ada variabel baru di `.env.example` (misal CyberPanel/Cloudflare) yang perlu ditambahkan, lalu sesuaikan `**Template Version:**` di `.workspaces/PROGRESS.md`.
4. **Verifikasi fase aktif.** Sebelum mengerjakan tugas apa pun, nyatakan secara eksplisit ke user: "Saya melanjutkan dari [nama fase] — saya akan [tindakan berikutnya]." Tunggu konfirmasi singkat jika ada perubahan dari ekspektasi.
5. **Jangan asumsikan — verifikasi.** Jika `.workspaces/PROGRESS.md` tidak ada, buat terlebih dahulu sebelum melanjutkan.

## Standard Operating Procedure (SOP)

Urutan kerja wajib diikuti secara berurutan. Jangan loncat fase. **Patuhi Guardrails pada tiap fase dengan ketat!**

**ATURAN UMUM PROGRESS:** Setiap kali satu tugas atau fase selesai, agen **WAJIB seketika itu juga (real-time)** mencatatnya ke dalam `.workspaces/PROGRESS.md`. Jangan menunggu sampai akhir proyek.

---

### Fase 1: Setup & Environment (Manusia & Agen)

Clone repo ini, buat file `.env` dari `.env.example`, isi `SITE.md` & `DESIGN.md`.
_(Skill terkait: Gunakan **`wpsk-editorial-brainstorm`** jika butuh bantuan AI untuk merumuskan niche, branding, dan sistem desain dari nol; gunakan **`wpsk-cyberpanel`** untuk provisi vhost/database/CMS otomatis di CyberPanel; gunakan **`wp-wpcli-and-ops`** untuk task operasional server/database awal jika diperlukan)._

**GUARDRAILS SETUP:**

- Agen **WAJIB** membuat folder wajib `.workspaces/assets/` di awal inisialisasi sebagai tempat menyimpan gambar (logo), featured image, placeholder, dll yang akan diunggah ke website.
- Segera inisialisasi file `.workspaces/PROGRESS.md` menggunakan template dari `PROGRESS.example.md`.
- User **WAJIB** menyediakan file `.env` berisi `WP_USERNAME` dan `WP_APP_PASSWORD` (Application Password role Administrator).
- User/Agen **WAJIB** menyiapkan file `.agents/mcp_config.json` dari `.agents/mcp_config.example.json` dengan domain target WordPress yang valid, dan memvalidasi koneksi ke **Easy MCP AI**.
- Agen **WAJIB** memeriksa ketersediaan **Pexafy MCP** (`search_photos`) di environment. Jika belum terpasang, agen wajib merekomendasikan instalasi Pexafy MCP kepada user.
- URL target diambil langsung dari field URL di `SITE.md`.
- Agen **WAJIB** memvalidasi koneksi ke WordPress REST API (`GET /wp-json/wp/v2/users/me`) menggunakan kredensial `.env` sebelum melangkah ke fase berikutnya.
- Agen **WAJIB** memverifikasi bahwa `DESIGN.md` terisi penuh — tidak ada field `{{ }}` yang tersisa.
- **Workflow Aset Brand Sekuensial (Prompt Generator):** Setelah `DESIGN.md` final, agen wajib meng-generate 5 rangkaian prompt brand berantai (*sequential follow-up prompts*) untuk ChatGPT/Image Generator (Logo rasio 16:5 tanpa tagline, Logo Inverse, Favicon 1:1, Favicon Rounded dengan backdrop circular, dan OG Image 1200x630) mengacu pada `wpsk-editorial-brainstorm`. Setiap prompt **wajib ditulis dalam satu paragraf penuh mengalir (tanpa bullet point / break)** dan digenerate dinamis secara instruksional (tanpa template engine kaku). Hasilnya disimpan pengguna di `.workspaces/assets/`.

---

### Fase 2: Perencanaan Arsitektur & PRD (@architect)

Sebelum koding tema atau penulisan konten dimulai, agen `@architect` **WAJIB** menyusun dokumen PRD di `PRODUCT.md` (pastikan file ini terdaftar di `.gitignore`).
_(Skill terkait: Merujuk pada panduan arsitektur visual di **`wpsk-theme-craft`** [perintah `shape`] dan hierarki template di **`wpsk-theme-convention`**)._

**GUARDRAILS PRD (`PRODUCT.md`):**

- Dokumen `PRODUCT.md` wajib memuat secara detail:
  1. **Daftar Template yang Akan Dibuat:** Seluruh template file yang direncanakan (`front-page.php`, `header.php`, `footer.php`, `single.php`, `author.php` [WAJIB], `page.php`, `archive.php`, `search.php`, `404.php`, dan komponen di `template-parts/`).
  2. **Struktur Wireframe & Layout yang Kaya Variasi:**
     - **Frontpage:** Wajib merancang **variasi layout section per kategori** (bukan grid 3 kolom yang diulang-ulang). Wajib memuat kombinasi Hero Headline Grid (1 featured besar + 3 stacked), Card Grid, Split Lead Article + List, Trending Block bernomor 1–5, dan **Pagination Frontpage** yang mengarah ke archive page tertentu.
     - **Header:** Spesifikasi container logo adaptif (Site Title teks ATAU Logo gambar dengan batas container terukur anti-meluap).
     - **Single Article:** Post header (judul, meta, kategori, author), featured media container, **Tombol Bagikan Social Share** (minimal 6 kanal: WhatsApp, Telegram, Facebook, X/Twitter, Threads, dan Copy Link dengan feedback visual), **Author Bio Box** lengkap, **Comment Box ter-styling Tailwind penuh**, **Custom Sidebar komponen** (bukan dynamic widget bawaan WP), breadcrumbs, konten Gutenberg layout, dan related posts.
     - **Author Archive (`author.php`):** Profil header penulis (avatar besar, nama, bio, jumlah artikel) + grid arsip artikel penulis tersebut.
- **HARD GATE PRD:** Dokumen `PRODUCT.md` harus ditinjau dan disetujui oleh User sebelum lanjut ke fase berikutnya. **Catat persetujuan ini di `.workspaces/PROGRESS.md`.**

---

### Fase 3: Fondasi Konten, Penulis, & Menu Navigasi (@content)

> **PRINSIP CONTENT-FIRST:**
> Fase ini dieksekusi **sebelum** koding tema dimulai. `@engineer` membutuhkan konten, kategori, author, dan menu navigasi nyata di WordPress agar saat tema dibangun, tema langsung terhubung ke data riil tanpa tebakan.

**ATURAN UTAMA KONTEN & REST API:**
- Seluruh manajemen konten (pembuatan author, kategori, tag, menu navigasi, halaman statis, dan artikel) **WAJIB** menggunakan **WordPress REST API** dengan Basic Auth Application Password atau **Easy MCP AI**.
- Pencarian featured image editorial **WAJIB** menggunakan **Pexafy MCP** (`search_photos`), diunduh dan diunggah via REST API sebagai post thumbnail.
- Wajib mematuhi aturan baku di **`.agents/rules/content-integrity.md`**:
  * Buat 3–5 user role `author` dengan diversitas nama multi-etnis Indonesia (anti-Dimas/Pramesti).
  * Format email: `<username>@<site.com>`.
  * DILARANG menerbitkan artikel atas nama user admin (wajib rotasi author merata).
  * Eksekusi penulisan artikel SEO Gutenberg secara paralel via subagent (`wpsk-seo-writer` dan `wp-patterns`).

---

### Fase 4: Pengembangan Tema Kustom (@engineer)

> **FASE INI DIMULAI SETELAH KONTEN & MENU SUDAH TERSEDIA DI WORDPRESS.**
> `@engineer` membangun tema dengan data nyata yang sudah ada di database WordPress.

**INSTRUKSI PERTAMA @engineer:**
Pelajari dan terapkan pedoman teknis dari:
1. **`.agents/rules/theme-guardrails.md`** — 8 aturan baku teknis tema WordPress `_tw` + Tailwind.
2. **`wpsk-theme-convention`** — spesifikasi teknis arsitektur tema WordPress `_tw` + Tailwind.
3. **`wpsk-theme-craft`** — aturan Craft Floor, anti-slop visual, tipografi editorial, dan perintah Impeccable (`polish`, `bolder`, `quieter`, `typeset`).
4. **`antislop-copywriting`** — eliminasi jargon AI pada copy/teks statis tema (CTA, placeholder, header, footer, microcopy).

**GUARDRAILS UTAMA TEMA:**
- `DESIGN.md` dan `PRODUCT.md` adalah **Sumber Kebenaran Mutlak**. Dilarang mengubah layout atau warna tanpa izin user.
- Koding dilakukan lokal di `.workspaces/theme-src/`. Dilarang edit langsung output build `theme/style.css` dan `theme/js/`.
- Dilarang Tailwind CDN; wajib PostCSS build.
- Output `.zip` dari `npm run bundle` **wajib diletakkan di root `.workspaces/`**.
- Generate `.workspaces/THEME_SPECS.md` setelah bundling tema.

---

### Fase 5: QA, Audit, & Verifikasi Visual (@qa)

Audit menyeluruh sebelum promosi situs:

- **Verifikasi Visual Otomatis (Playwright Screenshot):**
  * Agen `@qa` **wajib** menggunakan browser Playwright di background untuk membuka website live/staging.
  * Ambil **Full-Page Screenshot Desktop (1440px)** dan **Mobile (375px)** pada Homepage, Single Post, dan Author Archive.
  * Sematkan hasil screenshot langsung ke dalam dokumen **Artifact** Antigravity untuk review visual user yang instan tanpa perlu buka browser manual.
- **Audit Aksesibilitas & Kontras (`wpsk-theme-craft`):**
  * Jalankan kalkulator kontras Python (`contrast-check.py`) untuk memastikan seluruh teks memiliki rasio kontras minimal **4.5:1** (WCAG AA) dan elemen interaktif minimal **3:1**.
  * Pastikan navigasi keyboard memiliki `focus-visible` ring yang jelas.
- **Audit Responsivitas Mobile:**
  * Pastikan tidak ada horizontal overflow pada viewport 375px.
  * Pastikan ukuran tap target tombol/link minimal **44x44px**.
- **Audit Performa Backend & SEO:**
  * Profiling query SQL dan autoload options via **`wp-performance`**.
  * Validasi skor Lighthouse (Performance & SEO >= 80), broken links, dan sitemap XML.

---

### Fase 6: Deployment & Serah Terima (Manusia & Agen)

1. **Deploy Otomatis via CyberPanel (Opsional):**
   - Wajib patuhi protokol keselamatan di **`.agents/rules/cyberpanel-safety.md`**.
   - Agen **wajib menanyakan konfirmasi kepada user terlebih dahulu** sebelum melakukan upload otomatis ke server:
     *"Bundle tema .zip telah siap. Apakah Anda ingin tema diunggah dan diekstrak langsung ke server CyberPanel (`wp-content/themes/`)?"*
   - Jika disetujui, agen menjalankan:
     ```powershell
     python .agents/skills/wpsk-cyberpanel/scripts/cyberpanel_provisioner.py --domain <domain> --deploy-theme .workspaces/<theme-name>.zip
     ```
   - **Peringatan Wajib Pasca-Operasi:** Ingatkan user untuk segera menonaktifkan API Access pada CyberPanel (*Users > Modify User > API Access = Disable*).
2. **Deploy Manual:**
   - User mengaktifkan tema ZIP terbaru di dashboard WordPress `wp-admin → Appearance → Themes`.

---

## Workspace

Semua file pengerjaan agen **wajib disimpan di dalam folder `.workspaces/`**:

- **`.workspaces/assets/`** — logo, ilustrasi, thumbnail, dan aset visual.
- **`.workspaces/theme-src/`** — source code tema (PHP, CSS, JS, `package.json`).
- **`.workspaces/scripts/`** — skrip otomasi sementara.
- **`.workspaces/temp/`** — file temporer / log.
- **`.workspaces/THEME_SPECS.md`** — dokumen handover teknis tema.
- **`.workspaces/PROGRESS.md`** — dokumen pelacakan progres proyek (real-time).

**Aturan Ketat:**
- Dilarang menumpuk file campuran di root `.workspaces/`.
- Dilarang membuat file baru di luar `.workspaces/` kecuali file sistem repo utama (`AGENTS.md`, `README.md`, `.gitignore`, `.env.example`, `.agents/`).

## Conventions

- Awalan nama custom skill wajib menggunakan `wpsk-`.
- Bahasa konten default: Indonesia editorial berkualitas tinggi.

## Matriks Penugasan Skill per Fase Kerja

| Fase Proyek | Peran Agen | Skill Kunci yang Ditugaskan |
| :--- | :--- | :--- |
| **Fase 1: Setup & Env** | `@architect` / User | `wpsk-editorial-brainstorm`, `wp-wpcli-and-ops` |
| **Fase 2: Arsitektur & PRD** | `@architect` | `wpsk-theme-craft` (shape/critique), `wpsk-theme-convention` |
| **Fase 3: Konten, Penulis, & Menu** | `@content` (Paralel Subagents) | `wpsk-seo-writer` (diversitas author & anti-slop), `wp-patterns` |
| **Fase 4: Pengembangan Tema** | `@engineer` | `wpsk-theme-convention` (PHP _tw), `wpsk-theme-craft` (Craft Floor & polish), `antislop-copywriting` (anti-slop teks/copy statis tema), `wp-block-development` *(opsional)* |
| **Fase 5: QA & Verifikasi Visual** | `@qa` | `wpsk-theme-craft` (audit kontras Python & a11y), `wp-performance`, Playwright Screenshot |
| **Fase 6: Deployment & Ops** | Manusia & Agen | `wp-wpcli-and-ops`, `wpsk-cyberpanel` |
| **Meta Tooling** | Agen & Manusia | `skill-creator` |

## Boundaries (Jangan Lakukan)

- Jangan ubah wp-login atau pengaturan inti wp-admin tanpa persetujuan eksplisit.
- Jangan pernah memodifikasi konfigurasi server global, DNS Cloudflare, atau database CyberPanel tanpa meminta konfirmasi eksplisit dari user terlebih dahulu (lihat `.agents/rules/cyberpanel-safety.md`).
- **Wajib Peringatan Keamanan CyberPanel:** Agen WAJIB selalu mengingatkan pengguna untuk menonaktifkan fitur *API Access* pada user CyberPanel setiap kali selesai melakukan task/operasi server.
- Jangan unggah tema otomatis ke server tanpa menanyakan persetujuan user terlebih dahulu.
- Jangan gunakan FSE block theme penuh atau page builder berat (Elementor/Divi).
- Jangan hardcode kredensial WordPress di dalam file atau skrip; selalu baca dari `.env`.
- Jangan operasikan situs selain yang tercantum di `SITE.md`.
- Dilarang membuat artikel atas nama user admin (wajib rotasi author yang dibuat di Fase 3).
- Dilarang menggunakan nama author repetitif/klise (seperti Dimas atau Pramesti).
- Dilarang menulis artikel secara sekuensial jika dapat dijalankan secara paralel via subagent.
- Dilarang memulai koding tema sebelum PRD disetujui dan konten/menu diinjeksi.
- Jangan gunakan Tailwind CDN untuk tema (wajib PostCSS lokal).

## Definition of Done

PRD disetujui user, 3–5 author beragam terdaftar via REST API, taksonomi & menu Header/Footer terdaftar, artikel SEO Gutenberg paralel terbit dengan featured image dan author terdistribusi, tema dinamis selesai dibundle ke ZIP root `.workspaces/` (dengan container logo aman, frontpage variatif & terkonfigurasi dinamis, single post lengkap dengan tombol share 6 kanal, author box, styled comments, custom sidebar, `page.php` berkarakter editorial anti-polos, dan `author.php`), visual Desktop & Mobile terverifikasi via Playwright screenshot di Artifact, Lighthouse >=80, file `.workspaces/THEME_SPECS.md` digenerate.

## Changelog

### `10. 2026-09-29`

- **Refactoring Arsitektur Antigravity Harness:** Menerapkan best practice modular rules (`.agents/rules/`) untuk memecah batasan spesifik (`cyberpanel-safety.md`, `theme-guardrails.md`, `content-integrity.md`) dan menjaga ukuran `AGENTS.md` jauh di bawah batas 24KB harness.
- **Implementasi Lifecycle Hooks (`.agents/hooks.json`):** Menyediakan sistem hooks Antigravity untuk pengingat keamanan dan proteksi eksekusi server.

### `09. 2026-09-29`

- **Template Singular Page Anti-Polos (`page.php`):** Larangan keras membuat template singular page sekadar kotak putih polos biasa. Wajib hero page header elegan, wadah media sinematik, breadcrumb, dan tipografi Gutenberg luas.
- **Konfigurasi Dinamis Section Frontpage:** Larangan hardcode slug/ID kategori pada front-page, kewajiban fitur Theme Customizer / Options untuk judul/subtitle/kategori serta fallback dinamis otomatis (`get_categories()`).
- **Otomasi Deploy Tema CyberPanel:** Penambahan kapabilitas deploy otomatis arsip zip tema ke `wp-content/themes/` via CyberPanel dengan persetujuan eksplisit user.
- **Guardrails Keamanan Server & API Access CyberPanel:** Peringatan wajib konfirmasi sebelum modifikasi konfigurasi server serta pengingat rutin nonaktifkan API Access pasca-operasi.
- **Sistem Version Management Hemat Token:** Integrasi file `version.json` dan tracking versi di `PROGRESS.md` agar agen tidak membaca `UPDATE.md` jika versi sudah sesuai.

### `08. 2026-09-14`

- **Migrasi Integrasi MCP (Easy MCP AI & Pexafy):** Mengganti WPVibe dengan Easy MCP AI (melalui file konfigurasi `.agents/mcp_config.json`) untuk koneksi endpoint WordPress MCP, serta mengintegrasikan Pexafy MCP untuk pencarian gambar/featured image berkualitas tinggi.
- **Guardrail Inisialisasi MCP Fase 1:** Menambahkan kewajiban inisialisasi `.agents/mcp_config.json` dari template `.agents/mcp_config.example.json` serta pengecekan ketersediaan Pexafy MCP di awal proyek.

### `07. 2026-09-11`

- **Restrukturisasi Alur Kerja Content-First:** Memajukan pembuatan author, taksonomi, menu navigasi Header & Footer, dan artikel SEO Gutenberg (Fase 3) sebelum pembangunan tema (Fase 4), memastikan tema dikembangkan di atas data riil.
- **Integrasi Skill Terpadu `wpsk-theme-craft`:** Mengonsolidasikan 4 skill visual lama (`antislop-ui`, `antislop-human`, `antislop-layoutmobile`, `frontend-design`) menjadi 1 skill komprehensif yang mengadopsi 9 fungsi Impeccable (`shape`, `critique`, `audit`, `polish`, `bolder`, `quieter`, `distill`, `typeset`, `colorize`) dan Craft Floor.
- **8 Aturan Baku Pengalaman Lapangan:**
  1. Frontpage variasi column/section per kategori (Hero grid 1+3, 3-column cards, split list, trending).
  2. Container logo header aman anti-meluap (`max-h-12 md:max-h-14`, `object-contain`).
  3. Single post memuat Tombol Bagikan Social Share (minimal 6 kanal: WhatsApp, Telegram, Facebook, X, Threads, Copy Link dengan visual feedback).
  4. Single post memuat Author Box, Comment Box ter-styling Tailwind penuh, dan Custom Sidebar komponen.
  5. Frontpage pagination wajib mengarah ke Archive Page spesifik.
  6. Template `author.php` wajib ada (profil penulis + arsip artikel).
  7. Diversitas nama author Indonesia non-klise (larangan nama berulang seperti Dimas / Pramesti).
  8. Otomasi tangkapan layar Playwright Full-Page (Desktop 1440px & Mobile 375px) di Artifact pada Fase QA.
