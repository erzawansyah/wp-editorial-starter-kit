# Croco - Starter Kit Website Niche Editorial

Starter kit untuk produksi massal website niche blog/editorial berbasis WordPress, dioperasikan oleh AI agent (Antigravity) yang terhubung ke WordPress di server remote melalui WPVibe MCP.

## Cara Kerja

Repo ini bukan website. Repo ini adalah **cetakan** yang di-clone setiap kali ada permintaan pembuatan website baru. Setelah di-clone, operator mengisi identitas dan sistem desain, lalu AI mengeksekusi pembuatan konten dan tema berdasarkan spesifikasi tersebut secara sistematis.

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
    ├── assets/           # Direktori wajib aset (Logo, Gambar)
    ├── THEME_SPECS.md    # Dokumen handover teknis (digenerate oleh AI)
    └── PROGRESS.md       # Catatan live progres berjalan
```

## Prasyarat

- **Antigravity** sebagai AI client
- **WPVibe MCP** sudah terkonfigurasi dan terkoneksi ke situs WordPress target
- **Node.js + npm** terinstall di mesin lokal (untuk build Tailwind CSS)
- WordPress sudah terinstall di server dengan plugin dasar yang diperlukan
- **Tema GeneratePress** wajib diinstall di awal untuk memvalidasi kesiapan konten sebelum membangun tema kustom.

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
mkdir .workspaces/assets
```

### 3. Isi `SITE.md`

Buka `SITE.md`, isi semua field identitas website (nama, URL, niche, deskripsi, dsb.). Field yang masih berisi placeholder `{{ }}` akan memblokir AI dari mengerjakan apa pun - ini disengaja sebagai guard condition.

### 4. Setup WordPress di server

Ikuti checklist di [`WORDPRESS-SETUP.md`](WORDPRESS-SETUP.md) secara berurutan. Pastikan semua item centang sebelum lanjut - terutama koneksi WPVibe.

### 5. Isi `DESIGN.md`

Definisikan sistem desain: warna, tipografi, spacing, rounded corner, dan komponen. Gunakan [`DESIGN.example.md`](DESIGN.example.md) sebagai referensi nyata. YAML front matter di bagian atas harus terisi penuh.

### 6. Jalankan AI workflow

Buka Antigravity di direktori proyek. AI akan membaca `SITE.md` + `DESIGN.md` lalu mengikuti SOP ketat yang tercantum di `AGENTS.md`:

1. **Fase Setup** - Rename template, hapus index.php permalink, install GeneratePress, siapkan assets.
2. **Fase Konten** - generate kategori, halaman statis, logo, favicon, artikel SEO (Injeksi langsung ke DB). **Hard-Gate:** Tunggu persetujuan visual manusia.
3. **Fase Tema** - bangun tema classic kustom + Tailwind CSS dengan elemen fully dynamic (tanpa hardcode). Output file `.zip` dan file `.workspaces/THEME_SPECS.md` sebagai dokumentasi teknis akhir.
4. **Fase QA** - audit Lighthouse, broken link, responsivitas.

Update `.workspaces/PROGRESS.md` secara *real-time* setiap fase selesai.

### 7. Deploy

Setelah lolos QA dan mendapat approval, file tema zip siap diunggah oleh Manusia ke environment produksi.

## Alur Kerja (Workflow)

```text
Leader minta website baru
        │
        ▼
┌───────────────────────────────┐
│ Clone repo & isi SITE/DESIGN  │ ◄── Manusia
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
| JS Bundler | esbuild |
| Koneksi AI - WP | WPVibe MCP |
| AI Client | Antigravity |

## Konvensi Penting

- **Bahasa konten:** Indonesia, gaya editorial
- **File kerja AI & ZIP rilis** wajib disimpan di `.workspaces/`, dilarang mengotori root repo atau direktori tema sumber.
- **`SITE.md` di-gitignore** karena berisi data spesifik per proyek.
- **Anti-Dummy Rule:** AI dilarang membuat dummy lokal. Konten wajib diinjeksi via MCP.
- **Semua interaksi ke WordPress** dilakukan melalui WPVibe MCP, bukan command lokal.
