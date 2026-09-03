# Croco — Starter Kit Website Niche Editorial

Starter kit untuk produksi massal website niche blog/editorial berbasis WordPress, dioperasikan oleh AI agent (Antigravity) yang terhubung ke WordPress di server remote melalui WPVibe MCP.

## Cara Kerja

Repo ini bukan website. Repo ini adalah **cetakan** yang di-clone setiap kali ada permintaan pembuatan website baru. Setelah di-clone, operator mengisi identitas dan sistem desain, lalu AI mengeksekusi pembuatan konten dan tema berdasarkan spesifikasi tersebut.

## Struktur Repo

```
.
├── AGENTS.md             # Aturan kerja AI agent, SOP, dan boundaries
├── DESIGN.md             # Sistem desain (warna, tipografi, layout, komponen)
├── DESIGN.example.md     # Contoh DESIGN.md yang sudah terisi penuh
├── SITE.md               # Identitas website proyek saat ini (git-ignored)
├── SITE.example.md       # Template kosong SITE.md untuk proyek baru
├── WORDPRESS-SETUP.md    # Checklist instalasi WordPress + plugin wajib
├── PROGRESS.example.md   # Template checklist progres proyek
├── README.md             # File ini
├── skills-lock.json      # Lock file untuk skill yang digunakan
├── .gitignore
├── .agents/
│   ├── mcp_config.json   # Konfigurasi koneksi WPVibe MCP
│   └── skills/           # Skill AI agent
│       ├── theme-convention/   # Konvensi struktur tema classic + Tailwind
│       ├── antislop*/          # Skill kualitas kode, UI, copy, dan aksesibilitas
│       └── wp-*/               # Skill WordPress (REST API, blocks, performa, dsb.)
└── .workspaces/          # Output kerja AI per proyek (git-ignored)
    └── .gitkeep
```

## Prasyarat

- **Antigravity** sebagai AI client
- **WPVibe MCP** sudah terkonfigurasi dan terkoneksi ke situs WordPress target
- **Node.js + npm** terinstall di mesin lokal (untuk build Tailwind CSS via _tw)
- WordPress sudah terinstall di server dengan plugin dasar yang diperlukan
- **Tema _tw** sudah terinstall dan aktif di WordPress target (AI akan memandu jika belum ada)

## Memulai Proyek Baru

### 1. Clone repo

```bash
git clone <repo-url> nama-proyek
cd nama-proyek
```

### 2. Salin template file

```bash
cp SITE.example.md SITE.md
cp PROGRESS.example.md .workspaces/PROGRESS.md
```

### 3. Isi `SITE.md`

Buka `SITE.md`, isi semua field identitas website (nama, URL, niche, deskripsi, dsb.). Field yang masih berisi placeholder `{{ }}` akan memblokir AI dari mengerjakan apa pun — ini disengaja sebagai guard condition.

### 4. Setup WordPress di server

Ikuti checklist di [`WORDPRESS-SETUP.md`](WORDPRESS-SETUP.md) secara berurutan. Pastikan semua item centang sebelum lanjut — terutama koneksi WPVibe.

### 5. Isi `DESIGN.md`

Definisikan sistem desain: warna, tipografi, spacing, rounded corner, dan komponen. Gunakan [`DESIGN.example.md`](DESIGN.example.md) sebagai referensi nyata. YAML front matter di bagian atas harus terisi penuh.

### 6. Jalankan AI workflow

Buka Antigravity di direktori proyek. AI akan membaca `SITE.md` → `DESIGN.md` → lalu mengikuti SOP yang tercantum di `AGENTS.md`:

1. **Fase Konten** — kategori, halaman statis, logo, favicon, draft artikel
2. **Fase Tema** — wireframe, lalu build tema classic + Tailwind CSS
3. **Fase QA** — audit Lighthouse, broken link, responsivitas

Update `.workspaces/PROGRESS.md` setiap kali satu fase selesai.

### 7. Deploy

Setelah lolos QA dan mendapat approval, website siap dipromosikan ke environment produksi.

## Alur Kerja (Workflow)

```
Leader minta website baru
        │
        ▼
┌───────────────┐
│  Clone repo   │  ← manusia
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  Isi SITE.md  │  ← manusia
│  Isi DESIGN.md│
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  Install WP   │  ← manusia (server)
│  di server    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  @content     │  ← AI via WPVibe MCP
│  Konten & aset│
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  @architect   │  ← AI
│  Wireframe    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  @engineer    │  ← AI via WPVibe MCP
│  Build tema   │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  @qa          │  ← AI
│  Audit & test │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  Deploy       │  ← manusia
│  ke produksi  │
└───────────────┘
```

## Struktur Website yang Dihasilkan

Setiap website yang dibangun menggunakan starter kit ini mengikuti pola editorial standar:

- **Header:** Menu navigasi berisi kategori posting
- **Homepage:** Hero/headline grid + block artikel per kategori + trending
- **Sidebar:** Opsional
- **Footer:** Latest article + link halaman statis
- **Halaman statis:** Tim Redaksi, Tentang Kami, Kebijakan Privasi, dsb.
- **Template:** Single post, single page, archive kategori, search, 404

## Tech Stack

| Komponen | Teknologi |
|---|---|
| CMS | WordPress (PHP 8.2+) |
| Base Theme | [_tw](https://underscoretw.com/) — classic starter theme + Tailwind CSS |
| CSS Framework | Tailwind CSS (via PostCSS build, **bukan CDN**) |
| JS Bundler | esbuild (sudah include di _tw) |
| Koneksi AI ↔ WP | WPVibe MCP |
| AI Client | Antigravity |
| Skills | WordPress agent-skills, antislop |
| Build Environment | Node.js + npm (lokal, Windows 11)

## Konvensi Penting

- **Bahasa konten:** Indonesia, gaya editorial
- **File kerja AI** disimpan di `.workspaces/`, bukan di root
- **`SITE.md` di-gitignore** karena berisi data spesifik per proyek. Yang di-commit adalah `SITE.example.md` sebagai template
- **Guard condition:** AI dilarang bekerja jika `SITE.md` atau front matter `DESIGN.md` masih berisi placeholder `{{ }}`
- **Tema dibangun via draft/sandbox**, bukan langsung di tema aktif
- **Semua interaksi ke WordPress** dilakukan melalui WPVibe MCP, bukan command lokal

## File Referensi

| File | Fungsi |
|---|---|
| `SITE.md` | Identitas website (niche, URL, nama) — diisi per proyek |
| `DESIGN.md` | Sistem desain (warna, tipografi, layout, komponen) — diisi per proyek |
| `AGENT.md` | Aturan, SOP, dan batasan kerja AI agent |
| `SITE.example.md` | Template kosong `SITE.md` untuk proyek baru |
