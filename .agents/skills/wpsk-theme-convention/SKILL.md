---
# Skill: Theme Convention
name: wpsk-theme-convention
description: >
  Konvensi pengembangan tema berbasis _tw (underscore-tw) — WordPress starter
  theme dengan Tailwind CSS. Gunakan saat fase tema dimulai (@engineer).
  Semua keputusan struktur mengacu ke dokumen ini.
---

# Theme Convention — Berbasis _tw

## Stack

- **Base Theme:** [_tw](https://underscoretw.com/) — WordPress classic starter theme + Tailwind CSS
- **Build Tool:** PostCSS (Tailwind) + esbuild (JS), dijalankan lokal via npm
- **PHP:** 8.2+, Classic Theme (bukan Block Theme / FSE)
- **Node.js & npm:** wajib ada di mesin lokal operator

---

## Arsitektur _tw: Dua Lapisan

_tw memisahkan **source (build tools)** dari **output (tema WordPress)**:

> **Dokumentasi Referensi:**
> Folder `.agents/skills/theme-convention/references/` berisi dokumentasi resmi _tw (Installation, Development, Custom Blocks, dll.) yang bisa Anda baca kapan saja jika butuh panduan mendalam. Menggunakan `view_file` pada file-file tersebut sangat disarankan jika Anda menemui kendala.

```
.workspaces/{nama-proyek}/theme-src/   ← clone _tw, ada di lokal saja
│
├── tailwind.css          ← SOURCE: tulis Tailwind custom di sini
├── tailwind/             ← konfigurasi Tailwind (config, plugins)
├── javascript/
│   ├── script.js         ← SOURCE: JS frontend
│   └── block-editor.js   ← SOURCE: JS untuk WP editor
├── postcss.config.js
├── package.json          ← npm scripts (dev, watch, bundle)
│
└── theme/                ← OUTPUT: folder tema yang masuk ke WordPress
    ├── style.css         ← GENERATED — jangan edit manual
    ├── style-editor.css  ← GENERATED
    ├── functions.php     ← edit langsung via WPVibe atau lokal
    ├── header.php
    ├── footer.php
    ├── index.php
    ├── single.php
    ├── page.php
    ├── archive.php
    ├── search.php
    ├── 404.php
    ├── comments.php
    ├── theme.json
    ├── inc/              ← PHP helpers, includes
    ├── js/               ← GENERATED — jangan edit manual
    ├── languages/
    └── template-parts/   ← buat subfolder di sini sesuai kebutuhan
```

> **Aturan penting:**
> - File PHP di `theme/` → edit langsung via **WPVibe MCP** (atau lokal lalu upload)
> - File CSS/JS di `theme/` → jangan pernah edit manual, selalu **generate ulang via npm**
> - `tailwind.css` dan `javascript/` → edit lokal, lalu jalankan npm build

---

## Langkah 0: Cek Instalasi _tw di WordPress

**Wajib dilakukan sebelum mulai apapun.** Gunakan WPVibe untuk memverifikasi:

```
Via WPVibe rest_api:
GET /wp-json/wp/v2/themes?status=active
```

Atau: `list_files` di direktori `wp-content/themes/` dan cari tema berbasis _tw.

**Jika _tw belum terinstall** → ikuti prosedur instalasi di bawah. Jangan lanjut ke pengembangan sebelum tema terinstall dan aktif.

---

## Prosedur Instalasi _tw (jika belum ada)

### Opsi A: Via Web Generator (Rekomendasi)

1. Buka https://underscoretw.com/
2. Isi nama tema (gunakan slug dari `SITE.md`, misalnya `berita-foodies`)
3. Download zip hasil generate
4. Upload ke WordPress: **wp-admin → Appearance → Themes → Add New → Upload Theme**
5. Aktifkan tema tersebut

### Opsi B: Via WP-CLI (jika server punya WP-CLI)

```bash
wp package install gregsullivan/wp-cli-tw
wp tw generate --name="Nama Tema" --slug="nama-tema"
```

### Setelah Instalasi

1. Verifikasi tema aktif via WPVibe
2. Clone atau download source _tw ke lokal untuk build step:
   ```bash
   # Di dalam .workspaces/{nama-proyek}/
   npx degit gregsullivan/_tw theme-src
   cd theme-src
   npm install
   ```
3. Sesuaikan `theme/style.css` (header tema) dengan nama proyek

---

## Workflow Pengembangan

### Edit PHP Templates → via WPVibe (langsung di server)

File PHP di `theme/` bisa diedit langsung di server via WPVibe. Tidak perlu build step.

```
Gunakan WPVibe: edit_file atau write_file pada path:
wp-content/themes/{slug-tema}/header.php
wp-content/themes/{slug-tema}/footer.php
wp-content/themes/{slug-tema}/template-parts/...
dst.
```

### Edit CSS (Tailwind) → lokal + npm build + upload

1. Edit `tailwind.css` di lokal (`.workspaces/{proyek}/theme-src/tailwind.css`)
2. Konfigurasi warna dan font di `tailwind/` sesuai `DESIGN.md`
3. Build:
   ```bash
   npm run dev     # build sekali
   npm run watch   # watch + auto-rebuild saat development
   ```
4. Upload hasil build ke server via WPVibe:
   - `theme/style.css` → upload ke `wp-content/themes/{slug}/style.css`
   - `theme/style-editor.css` → upload ke `wp-content/themes/{slug}/style-editor.css`
   - `theme/js/` → upload ke `wp-content/themes/{slug}/js/`

### Deploy/Bundle ke Server

```bash
npm run bundle   # menghasilkan zip siap upload
```

Upload zip via wp-admin → Appearance → Themes → Upload, atau via WPVibe file management.

---

## Konfigurasi Tailwind dari DESIGN.md

Baca nilai dari `DESIGN.md` (front matter YAML), lalu terapkan ke `tailwind.css`:

```css
/* tailwind.css — contoh konfigurasi dari DESIGN.md */
@import "tailwindcss";

@theme {
  /* Colors dari DESIGN.md */
  --color-primary: #D94F3D;
  --color-secondary: #1A1A2E;
  --color-tertiary: #F4A823;
  --color-neutral: #F7F5F2;

  /* Typography dari DESIGN.md */
  --font-heading: "Playfair Display", serif;
  --font-body: "Inter", sans-serif;

  /* Spacing dari DESIGN.md */
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 32px;
}
```

> Nilai di atas hanya contoh. Selalu ambil dari `DESIGN.md` proyek yang sedang dikerjakan.

---

## Template Parts — Struktur yang Perlu Dibuat

_tw menyediakan `template-parts/` kosong. Buat subfolder sesuai kebutuhan editorial:

```
theme/template-parts/
├── content/
│   ├── content.php           ← loop artikel standar
│   └── content-none.php      ← jika tidak ada hasil
├── homepage/
│   ├── hero-grid.php         ← blok hero headline
│   ├── section-category.php  ← blok artikel per kategori (reusable)
│   └── section-trending.php  ← blok trending
└── post/
    ├── post-meta.php         ← byline: penulis, tanggal, kategori
    └── post-thumbnail.php    ← wrapper thumbnail
```

Panggil via:
```php
get_template_part( 'template-parts/homepage/hero-grid' );

// Dengan variabel (WP 5.5+)
get_template_part( 'template-parts/post/post-meta', null, [
    'show_author' => true,
] );
```

---

## npm Scripts Referensi

| Script | Fungsi |
|---|---|
| `npm run dev` | Build sekali (development, tidak di-minify) |
| `npm run watch` | Build + watch perubahan otomatis |
| `npm run bundle` | Build produksi + buat zip siap upload |

Jalankan semua perintah ini dari folder `.workspaces/{proyek}/theme-src/`.

---

## Do's and Don'ts

**Wajib:**
- Selalu cek instalasi _tw via WPVibe sebelum mulai fase tema
- Semua nilai warna dan font di Tailwind harus diambil dari `DESIGN.md`, bukan hardcode
- Escape semua output di PHP (`esc_html()`, `esc_url()`, `wp_kses_post()`)

**Dilarang:**
- Jangan edit `theme/style.css` atau `theme/js/` secara manual — akan ditimpa saat npm build
- Jangan gunakan Tailwind CDN Play — _tw menggunakan build pipeline PostCSS
- Jangan edit tema aktif di live langsung — semua perubahan PHP via WPVibe draft, CSS via build lokal

