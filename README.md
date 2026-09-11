# WP Editorial Starter Kit

Starter kit untuk produksi massal website niche blog/editorial berbasis WordPress, dioperasikan oleh AI agent (Antigravity) yang terhubung langsung ke WordPress via **WordPress REST API** (Application Password) serta didukung **WPVibe MCP** untuk operasi visual khusus seperti pencarian gambar.

## Cara Kerja

Repo ini bukan website. Repo ini adalah **cetakan** yang di-clone setiap kali ada permintaan pembuatan website baru. Setelah di-clone, operator mengisi kredensial `.env`, identitas `SITE.md`, dan sistem desain `DESIGN.md`. Selanjutnya, AI mengeksekusi perencanaan PRD (`PRODUCT.md`), penyusunan konten, kategori, author & menu terlebih dahulu (**Content-First**), pembangunan tema kustom lokal berbasis `_tw` + Tailwind CSS dengan standar visual **`wpsk-theme-craft`** (Impeccable Craft Floor), hingga verifikasi visual otomatis via Playwright.

## Struktur Repo

```text
.
├── AGENTS.md             # Aturan kerja AI agent, SOP 6 fase, dan boundaries (Single Source of Truth)
├── DESIGN.md             # Sistem desain: warna, tipografi, layout, komponen (git-ignored)
├── DESIGN.example.md     # Contoh DESIGN.md yang sudah terisi penuh
├── PRODUCT.md            # PRD: daftar template & wireframe detail frontpage/single (git-ignored)
├── SITE.md               # Identitas website & URL target proyek (git-ignored)
├── SITE.example.md       # Template kosong SITE.md untuk proyek baru
├── WORDPRESS-SETUP.md    # Checklist instalasi WordPress + Application Passwords
├── PROGRESS.example.md   # Template checklist pelacak progres proyek
├── README.md             # File dokumentasi ini
├── skills-lock.json      # Lock file untuk skill yang digunakan
├── .env.example          # Template kredensial WP REST API
├── .gitignore
├── .agents/
│   └── skills/           # 9 Skill AI agent aktif
│       ├── wpsk-editorial-brainstorm/ # Brainstorming konsep, niche, dan branding
│       ├── wpsk-theme-convention/     # Konvensi tema classic + Tailwind (_tw) & 8 aturan baku
│       ├── wpsk-theme-craft/          # Impeccable Design Director, Craft Floor, a11y, & audit kontras
│       ├── wpsk-seo-writer/           # Penulis SEO editorial Indonesia, anti-slop, diversitas author
│       ├── wp-patterns/               # Format sintaksis blok Gutenberg murni
│       ├── wp-block-development/      # Referensi pengembangan custom block
│       ├── wp-performance/            # Audit performa dan optimasi backend
│       ├── wp-wpcli-and-ops/          # Otomasi sistem dan database via WP-CLI
│       └── skill-creator/             # Pembuatan dan optimasi custom skill
└── .workspaces/          # Output kerja AI per proyek (git-ignored)
    ├── assets/           # Direktori wajib aset (Logo, Gambar, Favicon)
    ├── theme-src/        # Source code tema (PHP, CSS, JS — lokal)
    ├── scripts/          # Skrip otomasi sementara
    ├── temp/             # File temporer (log, dump JSON)
    ├── THEME_SPECS.md    # Dokumen handover teknis tema
    └── PROGRESS.md       # Catatan live progres berjalan (sumber kebenaran sesi)
```

## Prasyarat

- **Antigravity** sebagai AI client
- **Node.js + npm** terinstall di mesin lokal (untuk build Tailwind CSS)
- **WordPress** berjalan di server target (PHP 8.2+)
- **Application Password** WordPress ber-role Administrator (dikonfigurasi di `.env`)
- **WPVibe MCP** aktif di Antigravity (digunakan untuk pencarian gambar & operasi visual pelengkap)

## Memulai Proyek Baru

### 1. Clone repo

```bash
git clone <repo-url> nama-proyek
cd nama-proyek
```

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

Jika Anda sudah memiliki visi yang jelas, langsung isi file `SITE.md` dan `DESIGN.md`. Namun jika Anda **hanya memiliki nama domain**:
👉 **Panggil skill AI:** Ketik `/wpsk-editorial-brainstorm` di chat Antigravity. Agen akan memandu interview, merumuskan ide, dan mengisikan `SITE.md` serta `DESIGN.md` secara otomatis.

_(Catatan: Field `{{ }}` yang masih kosong akan memblokir AI dari mengeksekusi alur utama)_.

### 4. Setup WordPress di Server

Ikuti checklist di [`WORDPRESS-SETUP.md`](WORDPRESS-SETUP.md) secara berurutan. Pastikan permalink sudah diatur ke `/%postname%/` dan Application Password berfungsi normal.

### 5. Jalankan AI Workflow Utama (SOP 6 Fase)

Buka Antigravity di direktori proyek. AI akan menjalankan alur kerja terstruktur:

1. **Fase 1: Setup & Environment** — Verifikasi `.env`, validasi `SITE.md` & `DESIGN.md`, dan tes koneksi REST API.
2. **Fase 2: Arsitektur & PRD (@architect)** — Menyusun dokumen `PRODUCT.md` (spesifikasi template & wireframe detail: variasi layout section per kategori, container logo aman, single post dengan tombol share 6 kanal & author box, custom sidebar, pagination frontpage, dan author archive). **Hard-Gate:** Menunggu persetujuan user.
3. **Fase 3: Fondasi Konten, Penulis, & Menu Navigasi (@content)** — **Content-First**: Membuat 3–5 akun user `author` beragam (anti-Dimas/Pramesti), membuat taksonomi (kategori & tag), menetapkan struktur Menu Header & Footer di WordPress, serta memproduksi artikel SEO Gutenberg secara paralel via subagents (`wpsk-seo-writer` + `wp-patterns`).
4. **Fase 4: Pengembangan Tema Kustom (@engineer)** — Membangun tema kustom dinamis `_tw` + Tailwind CSS di atas data nyata mengacu pada `wpsk-theme-convention` dan `wpsk-theme-craft`. Menghasilkan file ZIP tema di root `.workspaces/` dan `THEME_SPECS.md`.
5. **Fase 5: QA, Audit, & Verifikasi Visual (@qa)** — Mengambil Full-Page Screenshot Desktop (1440px) dan Mobile (375px) via Playwright di Artifact, audit kontras teks WCAG min 4.5:1 via script Python, mobile tap target >= 44px, zero horizontal overflow 375px, dan audit Lighthouse >= 80.
6. **Fase 6: Deployment & Launch (Manusia & Agen)** — Unggah file ZIP tema terbaru dan website seketika tampil hidup dan proporsional bersama konten yang sudah siap.

Update `.workspaces/PROGRESS.md` secara _real-time_ setiap fase selesai.

---

## Diagram Alur Kerja (Workflow)

```text
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
│ Fase 2: Perencanaan & PRD (@architect)                 │ ◄── AI (wpsk-theme-craft: shape)
│ Susun PRODUCT.md (Wireframe Variatif, Logo, Share, dll)│
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ [HARD GATE] Validasi PRD                               │ ◄── User
│ Review & Persetujuan Dokumen PRODUCT.md                │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 3: Fondasi Konten, Penulis, & Menu (@content)     │ ◄── AI via REST API (Content-First)
│ 1. Buat 3-5 Author Beragam (Anti-Dimas/Pramesti)       │
│ 2. Buat Kategori, Tag, Menu Header & Footer di WP      │
│ 3. Publikasi Artikel SEO Gutenberg Paralel (Subagents) │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 4: Pengembangan Tema Kustom (@engineer)           │ ◄── AI (Data WP Sudah Siap!)
│ Koding _tw + Tailwind berpedoman wpsk-theme-convention │
│ dan wpsk-theme-craft (Craft Floor & Polish)            │
│ ──► Serahkan file ZIP tema di root .workspaces/       │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 5: QA, Audit, & Verifikasi Visual (@qa)           │ ◄── AI
│ 1. Playwright Screenshot Desktop (1440px) & Mobile     │
│ 2. Audit Kontras Python WCAG 4.5:1 & Tap Target 44px   │
│ 3. Audit Lighthouse >=80 & Backend wp-performance      │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Fase 6: Deployment & Serah Terima                      │ ◄── User
│ Upload ZIP Tema Final, Website Langsung Utuh & Live!   │
└────────────────────────────────────────────────────────┘
```

## Tech Stack

| Komponen | Teknologi |
| :--- | :--- |
| CMS | WordPress (PHP 8.2+) |
| Manajemen Konten | WordPress REST API murni (Application Password via `.env`) |
| Pencarian Gambar | WPVibe MCP (`search_images`) / Media Library |
| Base Theme | [\_tw](https://underscoretw.com/) (Classic starter theme) |
| CSS Framework | Tailwind CSS (via PostCSS build lokal, **bukan CDN**) |
| Standar Visual | `wpsk-theme-craft` (Impeccable Craft Floor & 9 Perintah) |
| JS Bundler | esbuild |
| AI Client | Antigravity |

## Konvensi Penting

- **Bahasa konten:** Indonesia, gaya editorial.
- **File kerja AI & ZIP rilis:** Wajib disimpan di `.workspaces/`, dilarang mengotori root repo atau folder tema sumber.
- **File `.env`, `SITE.md`, `DESIGN.md`, dan `PRODUCT.md` di-gitignore** karena berisi data spesifik per proyek.
- **Content-First:** Konten, kategori, penulis, dan menu navigasi dibuat sebelum tema kustom dikoding agar tema langsung terhubung ke data nyata.
- **Multi-Author Mandatory & Diversitas Nama:** Dilarang menerbitkan artikel atas nama admin. Wajib membuat 3–5 akun user author (`<username>@<site.com>`) dengan variasi nama realistis lintas etnis (bebas dari nama berulang seperti Dimas atau Pramesti).
- **Penulisan Paralel:** Penulisan artikel wajib dilakukan secara paralel menggunakan subagents untuk efisiensi dan keragaman sudut pandang.
