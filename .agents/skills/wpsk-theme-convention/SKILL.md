---
name: wpsk-theme-convention
description: >
  Konvensi pengembangan tema berbasis _tw (underscore-tw) — WordPress classic
  starter theme dengan Tailwind CSS. Gunakan saat fase tema dimulai (@engineer).
  Semua keputusan struktur mengacu ke dokumen ini.
---

# Theme Convention — Berbasis \_tw

> **BACA INI SEBELUM MENYENTUH SATU BARIS PUN KODE TEMA.**
> Skill ini adalah satu-satunya referensi teknis untuk fase pengembangan tema. Prioritasnya di bawah `AGENTS.md` — jika ada konflik, `AGENTS.md` menang. Jika ada konflik antara skill ini dengan instruksi ad hoc dari percakapan, skill ini menang.

---

## Prasyarat Wajib Sebelum Memulai

Sebelum menulis satu baris kode pun, verifikasi tiga kondisi ini di `.workspaces/PROGRESS.md`:

**1. Hard-Gate PRD Sudah Dilewati:**
Baris "HARD GATE: PRD disetujui oleh user" **wajib sudah dicentang**. Jika belum, **BERHENTI**. Minta `@architect` untuk menyelesaikan dokumen PRD di `PRODUCT.md`.

**2. Konten, Penulis, & Menu Navigasi Sudah Siap (Content-First):**
Fase Fondasi Konten & Menu **wajib sudah selesai**. Kategori, tag, 3–5 user author, menu navigasi Header & Footer, dan artikel real via REST API sudah terbit di server target. `@engineer` membangun tema di atas **data dan taksonomi riil**, bukan asumsi dummy.

**3. PRODUCT.md & DESIGN.md Sudah Final:**
`PRODUCT.md` menentukan daftar template dan wireframe detail, sedangkan `DESIGN.md` menentukan token desain (warna, tipografi, komponen). Tidak boleh ada field placeholder `{{ }}` yang tersisa.

---

## Stack

- **Base Theme:** [\_tw](https://underscoretw.com/) — WordPress classic starter theme + Tailwind CSS
- **Build Tool:** PostCSS (Tailwind v4) + esbuild (JS), dijalankan **LOKAL** via npm
- **Desain & Anti-Slop:** Berpedoman mutlak pada skill `wpsk-theme-craft` (Craft Floor & 9 Fungsi Impeccable)
- **PHP:** 8.2+, Classic Theme (bukan Block Theme / FSE)
- **Node.js & npm:** wajib ada di mesin lokal operator

---

## Arsitektur \_tw: Source vs Output

\_tw memisahkan **source code (yang diedit)** dari **output tema WordPress (yang di-generate)**:

```text
.workspaces/theme-src/          ← ROOT SOURCE (clone _tw, ada di lokal saja)
│
├── tailwind.css                ← EDIT DI SINI: custom Tailwind (warna, font dari DESIGN.md)
├── tailwind/                   ← konfigurasi Tailwind (config, plugins)
├── javascript/
│   ├── script.js               ← EDIT DI SINI: JS frontend
│   └── block-editor.js         ← EDIT DI SINI: JS untuk WP editor
├── postcss.config.js
├── package.json                ← npm scripts (dev, watch, bundle)
│
└── theme/                      ← OUTPUT TEMA (folder ini yang masuk ke WordPress)
    ├── style.css               ← GENERATED — jangan pernah edit manual
    ├── style-editor.css        ← GENERATED — jangan pernah edit manual
    ├── functions.php           ← EDIT LANGSUNG (deklarasi support, enqueue, dll.)
    ├── header.php
    ├── footer.php
    ├── front-page.php          ← template homepage (buat jika belum ada)
    ├── single.php              ← template artikel single post
    ├── author.php              ← WAJIB: template arsip profil author
    ├── index.php
    ├── page.php
    ├── archive.php
    ├── search.php
    ├── 404.php
    ├── comments.php
    ├── theme.json
    ├── inc/                    ← PHP helpers, custom functions
    ├── js/                     ← GENERATED — jangan pernah edit manual
    ├── languages/
    └── template-parts/         ← EDIT LANGSUNG: buat subfolder sesuai kebutuhan
```

> **Aturan Paling Kritis:**
>
> - File `theme/style.css` dan `theme/js/` adalah **output** dari proses build npm. **JANGAN PERNAH EDIT SECARA MANUAL** — akan ditimpa setiap kali `npm run dev` dijalankan.
> - **JANGAN GUNAKAN TAILWIND CDN** (`<script src="https://cdn.tailwindcss.com">`). \_tw menggunakan build pipeline PostCSS. CDN Tailwind akan menghasilkan CSS yang tidak ter-purge dan tidak konsisten.

---

## Prosedur Inisialisasi Tema (Jika Belum Ada)

Seluruh proses ini dilakukan **secara lokal**.

### Langkah 1: Generate Tema via underscoretw.com
1. Buka [https://underscoretw.com/](https://underscoretw.com/)
2. Isi **Theme Name** dengan nama situs dari `SITE.md` (contoh: `Rumah Desain`)
3. Isi **Theme Slug** dengan slug situs dari `SITE.md` (contoh: `rumah-desain`)
4. Download zip hasil generate
5. Ekstrak zip tersebut ke `.workspaces/theme-src/`

### Langkah 2: Install Dependencies & Build
```bash
cd .workspaces/theme-src
npm install
npm run dev
```

### Langkah 3: Rename Header Tema
Buka `theme/style.css` dan pastikan nama tema sesuai `SITE.md`.

---

## Konfigurasi Tailwind dari DESIGN.md

Buka `DESIGN.md`, catat nilai warna, font, dan spacing. Terapkan ke `tailwind.css`:

```css
/* .workspaces/theme-src/tailwind.css */
@import "tailwindcss";

@theme {
  /* Warna — ambil PERSIS dari DESIGN.md */
  --color-primary: #d94f3d;
  --color-secondary: #1a1a2e;
  --color-accent: #f4a823;
  --color-neutral: #f7f5f2;
  --color-text: #1a1a1a;

  /* Tipografi — ambil nama font dari DESIGN.md */
  --font-heading: "Playfair Display", serif;
  --font-body: "Inter", sans-serif;
}
```

---

## functions.php — Deklarasi Wajib

`functions.php` **wajib** mengandung deklarasi-deklarasi berikut:

```php
<?php
function starter_theme_setup() {
    // Navigasi: daftarkan lokasi menu
    register_nav_menus( [
        'primary' => __( 'Menu Utama', 'starter-theme' ),
        'footer'  => __( 'Menu Footer', 'starter-theme' ),
    ] );

    // Custom Logo: batasi ukuran terukur agar tidak meluap
    add_theme_support( 'custom-logo', [
        'height'      => 60,
        'width'       => 240,
        'flex-height' => true,
        'flex-width'  => true,
    ] );

    // Post Thumbnails
    add_theme_support( 'post-thumbnails' );

    // HTML5 support
    add_theme_support( 'html5', [
        'search-form', 'comment-form', 'comment-list', 'gallery', 'caption',
    ] );

    // Title tag
    add_theme_support( 'title-tag' );
}
add_action( 'after_setup_theme', 'starter_theme_setup' );
```

---

## Aturan Baku Elemen Dinamis & Tata Letak (Wajib Dipatuhi)

### 1. Header & Container Logo (Anti-Meluap)
Header **wajib disiapkan untuk mendukung Site Title teks ATAU Logo gambar** tanpa mengubah tinggi atau merusak container header:
* Container logo **wajib** memiliki batasan tinggi (`max-h-12 md:max-h-14`) dan properti `object-contain flex-shrink-0`.
* Logo tidak boleh meluap (*overflow*) dari navbar pada viewport apapun.

```php
<!-- header.php: BENAR & AMAN DARI OVERFLOW -->
<div class="site-branding flex items-center max-h-12 md:max-h-14 overflow-hidden">
    <?php if ( has_custom_logo() ) : ?>
        <div class="site-logo flex items-center [&_img]:max-h-12 md:[&_img]:max-h-14 [&_img]:w-auto [&_img]:object-contain">
            <?php the_custom_logo(); ?>
        </div>
    <?php else : ?>
        <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="font-heading font-bold text-xl md:text-2xl text-text hover:text-primary transition-colors">
            <?php bloginfo( 'name' ); ?>
        </a>
    <?php endif; ?>
</div>
```

### 2. Navigasi Header & Footer — Selalu `wp_nav_menu()`
```php
<?php wp_nav_menu( [
    'theme_location' => 'primary',
    'menu_class'     => 'flex items-center gap-6 text-sm font-medium',
    'container'      => false,
    'fallback_cb'    => false,
] ); ?>
```

### 3. Frontpage: Variasi Section per Kategori & Pagination Wajib
Halaman depan (`front-page.php`) **dilarang monoton**. Wajib menerapkan variasi struktur kolom/tata letak per kategori:
* **Hero Headline Grid:** 1 Featured Post besar di kiri + 3 stacked posts di kanan.
* **Section Kategori A:** 3-column card grid dengan thumbnail rasio 16:9.
* **Section Kategori B:** Split 2-column (1 lead article dengan excerpt + 3 compact horizontal list items).
* **Section Kategori C:** 4-column horizontal card strip atau list magazine.
* **Trending / Populer:** Numbered list 1–5 dengan angka display besar.
* **Pagination Frontpage:** Bagian bawah Frontpage **wajib** memiliki tombol/navigasi pagination (misal: *"Jelajahi Semua Artikel"*) yang ketika diklik **mengarah ke Archive Page** tertentu (seperti `/artikel/` atau halaman blog archive).

### 4. Single Post: Author Box, Comment Box Ber-styling, Custom Sidebar, & Tombol Bagikan
Halaman artikel (`single.php`) **wajib** memuat:
* **Tombol Bagikan (Social Share) Wajib:** Disediakan via komponen `template-parts/post/social-share.php` (dapat diletakkan di bawah judul dan/atau di akhir artikel). Wajib memuat **minimal 6 kanal**:
  1. **WhatsApp:** `https://api.whatsapp.com/send?text=...`
  2. **Telegram:** `https://t.me/share/url?url=...&text=...`
  3. **Facebook:** `https://www.facebook.com/sharer/sharer.php?u=...`
  4. **X (Twitter):** `https://twitter.com/intent/tweet?url=...&text=...`
  5. **Threads:** `https://www.threads.net/intent/post?text=...`
  6. **Copy Link:** Tombol salin tautan dengan JavaScript `navigator.clipboard.writeText()` dan visual feedback instan (*"Tersalin!"*).
* **Author Box:** Avatar penulis (`get_avatar()`), nama penulis dengan link ke arsipnya (`get_author_posts_url()`), dan biografi (`get_the_author_meta('description')`).
* **Comment Box yang Ter-styling Penuh:** Form komentar (`comment_form()`) dan list komentar wajib diberi styling Tailwind penuh (input border, padding, button submit bergaya tema, list komentar berulir rapi). Dilarang membiarkan form unstyled bawaan WP.
* **Custom Sidebar Komponen:** Dilarang mengandalkan dynamic widget default WordPress yang unstyled. Buat komponen sidebar kustom (`template-parts/sidebar/sidebar-single.php`) berisi:
  1. Author bio ringkas.
  2. Popular / Trending posts (via `WP_Query`).
  3. Kategori pills / Newsletter CTA.

### 5. Template Author Archive (`author.php`) — Wajib Ada
Situs editorial berpusat pada kredibilitas penulis. File `author.php` **wajib dibuat**:
* **Author Profile Header:** Foto avatar besar, nama lengkap author, bio lengkap, badge/role author, dan total artikel yang dipublikasikan (`count_user_posts()`).
* **Author Posts Loop:** Grid/List seluruh artikel yang ditulis oleh author tersebut, dilengkapi dengan pagination native WordPress.

---

## Struktur Template Parts Wajib

```text
theme/template-parts/
├── content/
│   ├── content-card.php        ← card artikel untuk loop (homepage, archive, search)
│   ├── content-single.php      ← konten artikel single post (Gutenberg styled)
│   └── content-none.php        ← fallback jika query kosong
├── homepage/
│   ├── hero-grid.php           ← blok hero headline (1 lead + 3 stacked)
│   ├── section-cards.php       ← blok kategori grid 3 kolom
│   ├── section-split.php       ← blok kategori split lead + horizontal list
│   └── section-trending.php    ← blok trending bernomor 1-5
├── post/
│   ├── author-box.php          ← box profil author di single post
│   ├── social-share.php        ← tombol bagikan (WhatsApp, Telegram, FB, X, Threads, Copy Link)
│   ├── post-meta.php           ← byline: penulis, tanggal, reading time
│   └── post-thumbnail.php      ← wrapper featured image responsif
├── sidebar/
│   └── sidebar-single.php      ← custom sidebar single post
└── global/
    ├── site-branding.php       ← logo + site title anti-meluap
    └── pagination.php          ← navigasi halaman arsip / frontpage
```

---

## Checklist Fase Tema (Wajib Semua ✅ Sebelum Bundle)

- [ ] `PRODUCT.md` dan `DESIGN.md` dipatuhi secara penuh
- [ ] Skill `wpsk-theme-craft` (Craft Floor) sudah dipelajari dan dipenuhi
- [ ] Header aman: Container logo dibatasi (`max-h-12 md:max-h-14`), tidak meluap jika ada logo gambar
- [ ] Frontpage memiliki variasi section kategori yang kaya + pagination menuju archive
- [ ] Single post memuat Author Box, Comment Box ter-styling Tailwind, dan Custom Sidebar
- [ ] Template `author.php` sudah dibuat dan berfungsi menampilkan profil penulis + arsip artikelnya
- [ ] Tidak ada hardcode HTML untuk navigasi (selalu `wp_nav_menu()`)
- [ ] Tidak ada Tailwind CDN — build PostCSS lokal via `npm run dev`
- [ ] Output PHP di-escape (`esc_html()`, `esc_url()`, `wp_kses_post()`)
- [ ] `theme/screenshot.png` (1200x900px) sudah dibuat
- [ ] Bundle zip berada di root `.workspaces/` (bukan di dalam `theme-src/`)
- [ ] `.workspaces/THEME_SPECS.md` digenerate
