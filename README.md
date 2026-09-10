# WP Editorial Starter Kit

Starter kit untuk produksi massal website niche blog/editorial berbasis WordPress, dioperasikan oleh AI agent (Antigravity) yang terhubung ke WordPress di server remote melalui WPVibe MCP.
Starter kit untuk produksi massal website niche blog/editorial berbasis WordPress, dioperasikan oleh AI agent (Antigravity) yang terhubung langsung ke WordPress via **WordPress REST API** (Application Password) serta didukung **WPVibe MCP** untuk operasi visual khusus seperti pencarian gambar.

## Cara Kerja

Repo ini bukan website. Repo ini adalah **cetakan** yang di-clone setiap kali ada permintaan pembuatan website baru. Setelah di-clone, operator mengisi identitas dan sistem desain, lalu AI mengeksekusi pembuatan konten dan tema berdasarkan spesifikasi tersebut secara sistematis.
Repo ini bukan website. Repo ini adalah **cetakan** yang di-clone setiap kali ada permintaan pembuatan website baru. Setelah di-clone, operator mengisi kredensial `.env`, identitas `SITE.md`, dan sistem desain `DESIGN.md`. Selanjutnya, AI mengeksekusi perencanaan PRD (`PRODUCT.md`), pembangunan tema kustom secara lokal, pembuatan akun author, hingga penerbitan konten SEO secara paralel via subagent.
Repo ini bukan website. Repo ini adalah **cetakan** yang di-clone setiap kali ada permintaan pembuatan website baru. Setelah di-clone, operator mengisi kredensial `.env`, identitas `SITE.md`, dan sistem desain `DESIGN.md`. Selanjutnya, AI mengeksekusi perencanaan PRD (`PRODUCT.md`), pembangunan tema kustom secara lokal, pembuatan akun author, hingga penerbitan konten SEO secara paralel via subagent (menggunakan skill `wpsk-seo-writer`).

## Struktur Repo

```
```text
.
├── AGENTS.md             # Aturan kerja AI agent, SOP, dan boundaries
├── DESIGN.md             # Sistem desain (warna, tipografi, layout, komponen)
├── AGENTS.md             # Aturan kerja AI agent, SOP, dan boundaries (Single Source of Truth)
├── DESIGN.md             # Sistem desain: warna, tipografi, layout, komponen (git-ignored)
├── DESIGN.example.md     # Contoh DESIGN.md yang sudah terisi penuh
├── SITE.md               # Identitas website proyek saat ini (git-ignored)
├── PRODUCT.md            # PRD: daftar template & wireframe detail frontpage/single (git-ignored)
├── SITE.md               # Identitas website & URL target proyek (git-ignored)
├── SITE.example.md       # Template kosong SITE.md untuk proyek baru
├── WORDPRESS-SETUP.md    # Checklist instalasi WordPress + plugin wajib
├── PROGRESS.example.md   # Template checklist progres proyek
├── README.md             # File ini
├── WORDPRESS-SETUP.md    # Checklist instalasi WordPress + Application Passwords
├── PROGRESS.example.md   # Template checklist pelacak progres proyek
├── README.md             # File dokumentasi ini
├── skills-lock.json      # Lock file untuk skill yang digunakan
├── .env.example          # Template kredensial WP REST API
├── .gitignore
├── .agents/
│   ├── mcp_config.json   # Konfigurasi koneksi WPVibe MCP
│   └── skills/           # Skill AI agent
│       ├── wpsk-editorial-brainstorm/ # Skill interaktif untuk memandu pembuatan konsep website
│       ├── wpsk-theme-convention/     # Konvensi struktur tema classic + Tailwind (referensi wajib @engineer)
│       ├── antislop/                  # Skill anti-slop core (filter utama)
│       ├── wpsk-editorial-brainstorm/ # Brainstorming konsep, niche, dan branding
│       ├── wpsk-theme-convention/     # Konvensi tema classic + Tailwind (_tw)
│       ├── wpsk-seo-writer/           # Penulis SEO editorial Indonesia, anti-slop, GEO/AEO
│       ├── antislop/                  # Filter anti-slop core
│       ├── antislop-ui/               # Filter visual: warna, layout, komponen
│       ├── antislop-human/            # Aksesibilitas: kontras, keyboard, focus
│       ├── antislop-layoutmobile/     # Layout responsif & mobile
│       ├── antislop-human/            # Aksesibilitas: kontras, navigasi keyboard
│       ├── antislop-layoutmobile/     # Tata letak responsif & mobile-first
│       ├── antislop-code/             # Higiene komentar kode
│       ├── antislop-copywriting/      # Kualitas teks & copy
│       ├── antislop-copywriting/      # Kualitas tulisan & microcopy anti-AI
│       ├── frontend-design/           # Art direction & tipografi editorial
│       ├── seo-article/               # Standar penulisan artikel SEO
│       └── wp-*/                      # Skill WordPress (REST API, blocks, performa, dsb.)
│       ├── seo-article/               # Standar penulisan artikel SEO, AEO, GEO
│       └── wp-*/                      # Skill ekosistem WordPress
└── .workspaces/          # Output kerja AI per proyek (git-ignored)
    ├── assets/           # Direktori wajib aset (Logo, Gambar)
    ├── theme-src/        # Source code tema (PHP, CSS, JS — lokal saja)
    ├── assets/           # Direktori wajib aset (Logo, Gambar, Favicon)
    ├── theme-src/        # Source code tema (PHP, CSS, JS — lokal)
    ├── scripts/          # Skrip otomasi sementara
    ├── temp/             # File temporer (log, dump, draf)
    ├── THEME_SPECS.md    # Dokumen handover teknis (digenerate oleh AI)
    └── PROGRESS.md       # Catatan live progres berjalan (sumber kebenaran lintas sesi)
    ├── temp/             # File temporer (log, dump JSON)
    ├── THEME_SPECS.md    # Dokumen handover teknis tema
    └── PROGRESS.md       # Catatan live progres berjalan (sumber kebenaran sesi)
```

## Prasyarat

- **Antigravity** sebagai AI client
- **WPVibe MCP** sudah terkonfigurasi dan terkoneksi ke situs WordPress target
- **Node.js + npm** terinstall di mesin lokal (untuk build Tailwind CSS)
- WordPress sudah terinstall di server dengan plugin dasar yang diperlukan
- **Tema GeneratePress** wajib diinstall di awal untuk memvalidasi kesiapan konten sebelum membangun tema kustom.
- **WordPress** berjalan di server target (PHP 8.2+)
- **Application Password** WordPress ber-role Administrator (dikonfigurasi di `.env`)
- **WPVibe MCP** aktif di Antigravity (digunakan untuk pencarian gambar & operasi visual pelengkap)

## Memulai Proyek Baru

### 1. Clone repo

```bash
git clone <repo-url> nama-proyek
cd nama-proyek
```

### 2. Salin template file
### 2. Siapkan file konfigurasi & environment

```bash
cp SITE.example.md SITE.md
cp PROGRESS.example.md .workspaces/PROGRESS.md
cp .env.example .env
mkdir .workspaces/assets
```

Isi file `.env` dengan kredensial Application Password WordPress Anda:
```env
WP_USERNAME=admin_anda
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx
```

### 3. Setup Konsep (Opsional: Gunakan Bantuan AI)

Jika Anda sudah memiliki visi yang jelas, langsung buka dan isi file `SITE.md` dan `DESIGN.md`. Namun, jika Anda **hanya memiliki nama domain** dan kebingungan menentukan *niche*, warna, atau menu navigasi:
👉 **Panggil skill AI:** Ketik `/wpsk-editorial-brainstorm` di chat Antigravity. Agen akan meng-interview Anda, merumuskan ide, dan mengisikan `SITE.md` serta `DESIGN.md` secara otomatis untuk Anda!
Jika Anda sudah memiliki visi yang jelas, langsung isi file `SITE.md` dan `DESIGN.md`. Namun jika Anda **hanya memiliki nama domain**:
👉 **Panggil skill AI:** Ketik `/wpsk-editorial-brainstorm` di chat Antigravity. Agen akan memandu interview, merumuskan ide, dan mengisikan `SITE.md` serta `DESIGN.md` secara otomatis.

*(Catatan: Field `{{ }}` yang masih kosong akan memblokir AI dari mengeksekusi alur utama)*.

### 4. Setup WordPress di server
### 4. Setup WordPress di Server

Ikuti checklist di [`WORDPRESS-SETUP.md`](WORDPRESS-SETUP.md) secara berurutan. Pastikan semua item centang sebelum lanjut - terutama koneksi WPVibe.
Ikuti checklist di [`WORDPRESS-SETUP.md`](WORDPRESS-SETUP.md) secara berurutan. Pastikan permalink sudah diatur ke `/%postname%/` dan Application Password berfungsi normal.

### 5. Jalankan AI workflow Utama
### 5. Jalankan AI Workflow Utama

Buka Antigravity di direktori proyek. AI akan membaca spesifikasi Anda lalu mengikuti SOP ketat yang tercantum di `AGENTS.md`:
Buka Antigravity di direktori proyek. AI akan menjalankan SOP berikut secara berurutan:

1. **Fase Setup** - Rename template, hapus index.php permalink, install GeneratePress, siapkan assets.
2. **Fase Konten** - generate kategori, halaman statis, logo, favicon, artikel SEO (Injeksi langsung ke DB). **Hard-Gate:** Tunggu persetujuan visual manusia.
3. **Fase Tema** - bangun tema classic kustom + Tailwind CSS dengan elemen fully dynamic (tanpa hardcode). Output file `.zip` dan file `.workspaces/THEME_SPECS.md` sebagai dokumentasi teknis akhir.
4. **Fase QA** - audit Lighthouse, broken link, responsivitas.
1. **Fase 1: Setup & Environment** — Verifikasi `.env`, validasi `SITE.md` & `DESIGN.md`, dan tes koneksi REST API.
2. **Fase 2: Arsitektur & PRD (@architect)** — Menyusun dokumen `PRODUCT.md` (spesifikasi template & wireframe detail frontpage dan single article). **Hard-Gate:** Menunggu persetujuan user.
3. **Fase 3: Pengembangan Tema (@engineer)** — Membangun tema kustom dinamis `_tw` + Tailwind CSS secara lokal di `.workspaces/theme-src/`. Menghasilkan file ZIP tema di `.workspaces/` dan `THEME_SPECS.md`. ZIP tema diberikan kepada user setiap kali selesai atau ada perubahan tema.
4. **Fase 4: Manajemen Penulis & Konten (@content)** — Membuat 3–5 akun user role `author` via REST API dengan email `<username>@<site.com>`. Melakukan injeksi taksonomi & halaman statis, serta memproduksi artikel SEO Gutenberg **secara paralel via subagents** dengan atribusi author bergantian (bukan admin).
4. **Fase 4: Manajemen Penulis & Konten (@content)** — Membuat 3–5 akun user role `author` via REST API dengan email `<username>@<site.com>`. Melakukan injeksi taksonomi & halaman statis, serta memproduksi artikel SEO Gutenberg **secara paralel via subagents** (menggunakan skill `wpsk-seo-writer`) dengan atribusi author bergantian (bukan admin).
5. **Fase 5: QA (@qa)** — Audit Lighthouse (>=80), broken link check, uji responsivitas mobile/tablet/desktop.
6. **Fase 6: Deployment & Launch (Manusia)** — Unggah file ZIP tema terbaru dan validasi visual akhir bersama konten live.

Update `.workspaces/PROGRESS.md` secara *real-time* setiap fase selesai.

### 6. Deploy
---

Setelah lolos QA dan mendapat approval, file tema zip siap diunggah oleh Manusia ke environment produksi.
## Diagram Alur Kerja (Workflow)

## Alur Kerja (Workflow)

```text
Leader minta website baru
        │
        ▼
┌───────────────────────────────┐
│ Clone repo & Persiapan        │ ◄── Manusia
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ [OPSIONAL] @brainstorm        │ ◄── AI (Jika butuh ide)
│ Bantu perumusan konsep        │
│ & Auto-fill SITE/DESIGN       │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ @setup                        │ ◄── AI via WPVibe
│ Rename Tema, Permalinks,      │
│ Install GeneratePress         │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ @content                      │ ◄── AI via WPVibe
│ Injeksi Konten, Kategori, Page│
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ [HARD GATE] Validasi Konten   │ ◄── Manusia & AI
│ Review visual di GeneratePress│
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ @engineer                     │ ◄── AI
│ Build Tema Kustom (Dinamis)   │
│ Generate THEME_SPECS.md       │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ @qa                           │ ◄── AI
│ Audit Lighthouse & Responsif  │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Deploy (Manual Upload ZIP)    │ ◄── Manusia
└───────────────────────────────┘
               User Clone Repo & Setup .env
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ [OPSIONAL] @brainstorm                                 │ ◄── AI (Jika butuh ide)
│ Bantu perumusan konsep & Auto-fill SITE/DESIGN         │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 1: Setup & Environment                            │ ◄── AI & User
│ Verifikasi .env, REST API Ping, Setup Assets Folder    │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 2: Perencanaan & PRD (@architect)                 │ ◄── AI
│ Susun PRODUCT.md (Daftar Template & Wireframe Detail)  │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ [HARD GATE] Validasi PRD                               │ ◄── User
│ Review & Persetujuan Dokumen PRODUCT.md                │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 3: Pengembangan Tema (@engineer)                  │ ◄── AI
│ Koding Lokal _tw + Tailwind, Generate THEME_SPECS.md   │
│ ──► Serahkan file ZIP tema ke User saat selesai/ubah  │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 4: Manajemen Penulis & Konten (@content)          │ ◄── AI via REST API
│ 1. Buat 3-5 Author (<username>@<site.com>)             │
│ 2. Buat Kategori, Tag, Menu, Halaman Statis            │
│ 3. Penulisan Artikel Paralel via Subagents             │
│    (Gutenberg Blocks + Featured Image + Rotasi Author) │
│    (wpsk-seo-writer + Gutenberg + Rotasi Author)       │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 5: QA & Audit (@qa)                               │ ◄── AI
│ Audit Lighthouse >=80, Broken Links, Responsivitas     │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 6: Deployment & Serah Terima                      │ ◄── User
│ Upload ZIP Tema Final, Review Visual Bersama Konten   │
└────────────────────────────────────────────────────────┘
```

## Struktur Website yang Dihasilkan

Setiap website yang dibangun menggunakan starter kit ini mengikuti pola editorial standar:

- **Header:** Menu navigasi dinamis + Pencarian + Logo custom
- **Homepage:** Hero/headline grid + block artikel per kategori + trending
- **Sidebar:** Tersedia opsi Pagination/Widget
- **Footer:** Latest article + link halaman statis
- **Halaman statis:** Tim Redaksi, Tentang Kami, Kebijakan Privasi, Syarat & Ketentuan, Kontak.
- **Template:** Single post, single page, archive kategori, search, 404

## Tech Stack

| Komponen | Teknologi |
|---|---|
| CMS | WordPress (PHP 8.2+) |
| Base Theme | [_tw](https://underscoretw.com/) (Disesuaikan otomatis nama temanya) |
| CSS Framework | Tailwind CSS (via PostCSS build, **bukan CDN**) |
| Manajemen Konten | WordPress REST API murni (Application Password via `.env`) |
| Pencarian Gambar | WPVibe MCP (`search_images`) / Media Library |
| Base Theme | [_tw](https://underscoretw.com/) (Classic starter theme) |
| CSS Framework | Tailwind CSS (via PostCSS build lokal, **bukan CDN**) |
| JS Bundler | esbuild |
| Koneksi AI - WP | WPVibe MCP |
| AI Client | Antigravity |

## Konvensi Penting

- **Bahasa konten:** Indonesia, gaya editorial
- **File kerja AI & ZIP rilis** wajib disimpan di `.workspaces/`, dilarang mengotori root repo atau direktori tema sumber.
- **`SITE.md` di-gitignore** karena berisi data spesifik per proyek.
- **Anti-Dummy Rule:** AI dilarang membuat dummy lokal. Konten wajib diinjeksi via MCP.
- **Semua interaksi ke WordPress** dilakukan melalui WPVibe MCP, bukan command lokal.

- **Bahasa konten:** Indonesia, gaya editorial.
- **File kerja AI & ZIP rilis:** Wajib disimpan di `.workspaces/`, dilarang mengotori root repo atau folder tema sumber.
- **File `.env`, `SITE.md`, `DESIGN.md`, dan `PRODUCT.md` di-gitignore** karena berisi data spesifik per proyek.
- **Anti-Dummy Rule:** Konten artikel wajib berbobot riset tinggi dan diinjeksi langsung via WP REST API.
- **Multi-Author Mandatory:** Dilarang menerbitkan artikel atas nama admin. Wajib membuat 3–5 akun user author (`<username>@<site.com>`) dan mendistribusikan artikel ke author-author tersebut.
- **Penulisan Paralel:** Penulisan artikel wajib dilakukan secara paralel menggunakan subagents untuk efisiensi dan keragaman sudut pandang.
