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

Sebelum menulis satu baris kode pun, verifikasi dua kondisi ini:

**1. Hard-Gate PRD Sudah Dilewati:**
Cek `.workspaces/PROGRESS.md`. Baris "HARD GATE: PRD disetujui oleh user" **wajib sudah dicentang**. Jika belum, **BERHENTI**. Minta `@architect` untuk menyelesaikan dokumen PRD di `PRODUCT.md`.

**2. PRODUCT.md & DESIGN.md Sudah Final:**
Buka `PRODUCT.md` dan `DESIGN.md`. Keduanya adalah spesifikasi teknis mutlak: `PRODUCT.md` menentukan daftar template dan wireframe detail (frontpage & single article), sedangkan `DESIGN.md` menentukan token desain (warna, tipografi, komponen). Tidak boleh ada field placeholder `{{ }}` yang tersisa.

---

## Stack

- **Base Theme:** [\_tw](https://underscoretw.com/) — WordPress classic starter theme + Tailwind CSS
- **Build Tool:** PostCSS (Tailwind v4) + esbuild (JS), dijalankan **LOKAL** via npm
- **PHP:** 8.2+, Classic Theme (bukan Block Theme / FSE)
- **Node.js & npm:** wajib ada di mesin lokal operator

---

## Arsitektur \_tw: Source vs Output

\_tw memisahkan **source code (yang diedit)** dari **output tema WordPress (yang di-generate)**. Memahami perbedaan ini adalah aturan pertama:

```
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
    ├── index.php
    ├── single.php
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

Seluruh proses ini dilakukan **secara lokal**. Tidak ada langkah yang melibatkan WPVibe atau server remote.

### Langkah 1: Generate Tema via underscoretw.com

1. Buka [https://underscoretw.com/](https://underscoretw.com/)
2. Isi **Theme Name** dengan nama situs dari `SITE.md` (contoh: `Rumah Desain`)
3. Isi **Theme Slug** dengan slug situs dari `SITE.md` (contoh: `rumah-desain`)
4. Download zip hasil generate
5. Ekstrak zip tersebut ke `.workspaces/theme-src/`

### Langkah 2: Install Dependencies

```bash
# Jalankan dari root .workspaces/theme-src/
cd .workspaces/theme-src
npm install
```

### Langkah 3: Verifikasi Build Berjalan

```bash
npm run dev
```

Jika sukses, file `theme/style.css` akan ter-generate. Jika gagal, cek `package.json` dan pastikan Node.js >= 18.

### Langkah 4: Rename Header Tema

Buka `theme/style.css` dan ubah baris:

```css
Theme Name: _tw
```

Menjadi nama tema sesuai `SITE.md`. **Langkah ini wajib** sebelum langkah apapun lainnya.

---

## Konfigurasi Tailwind dari DESIGN.md

**Wajib dibaca lebih dulu:** Buka `DESIGN.md`, catat nilai warna, font, dan spacing. Kemudian terapkan ke `tailwind.css`:

```css
/* .workspaces/theme-src/tailwind.css */
@import "tailwindcss";

@theme {
  /* Warna — ambil PERSIS dari DESIGN.md, bukan tebakan */
  --color-primary: #d94f3d; /* contoh: ganti dengan nilai di DESIGN.md */
  --color-secondary: #1a1a2e;
  --color-accent: #f4a823;
  --color-neutral: #f7f5f2;
  --color-text: #1a1a1a;

  /* Tipografi — ambil nama font dari DESIGN.md */
  --font-heading: "Playfair Display", serif;
  --font-body: "Inter", sans-serif;
}
```

> **INGAT:** Nilai di atas adalah contoh. Selalu ambil nilai sesungguhnya dari `DESIGN.md` proyek yang sedang dikerjakan. Jangan pernah gunakan warna default Tailwind atau nilai inventif AI.

---

## functions.php — Deklarasi Wajib

`functions.php` **wajib** mengandung deklarasi-deklarasi berikut. Tambahkan jika belum ada:

```php
<?php
function nama_tema_setup() {
    // Navigasi: daftarkan semua lokasi menu
    register_nav_menus( [
        'primary' => __( 'Menu Utama', 'nama-tema' ),
        'footer'  => __( 'Menu Footer', 'nama-tema' ),
    ] );

    // Custom Logo: WAJIB ada untuk wp_nav_menu dan has_custom_logo()
    add_theme_support( 'custom-logo', [
        'height'      => 60,
        'width'       => 200,
        'flex-height' => true,
        'flex-width'  => true,
    ] );

    // Post Thumbnails: untuk featured image artikel
    add_theme_support( 'post-thumbnails' );

    // HTML5 support
    add_theme_support( 'html5', [
        'search-form', 'comment-form', 'comment-list', 'gallery', 'caption',
    ] );

    // Title tag
    add_theme_support( 'title-tag' );
}
add_action( 'after_setup_theme', 'nama_tema_setup' );
```

---

## Aturan Elemen Dinamis (Tidak Boleh Dilanggar)

Ini adalah aturan paling sering dilanggar AI. **Tidak ada pengecualian.**

### ✅ Navigasi — Selalu `wp_nav_menu()`

```php
<!-- header.php: BENAR -->
<?php wp_nav_menu( [
    'theme_location' => 'primary',
    'menu_class'     => 'flex gap-6 items-center',
    'container'      => false,
] ); ?>

<!-- DILARANG: hardcode HTML statis seperti ini -->
<!-- <ul><li><a href="/tentang">Tentang</a></li></ul> -->
```

### ✅ Logo — Selalu `the_custom_logo()`

```php
<!-- header.php: BENAR -->
<?php if ( has_custom_logo() ) : ?>
    <?php the_custom_logo(); ?>
<?php else : ?>
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="font-heading font-bold text-xl">
        <?php bloginfo( 'name' ); ?>
    </a>
<?php endif; ?>

<!-- DILARANG: hardcode img tag -->
<!-- <img src="/wp-content/uploads/logo.png" alt="Logo"> -->
```

### ✅ Query Artikel — Selalu WP_Query atau get_posts()

```php
<!-- section-category.php: BENAR -->
<?php
$args = [
    'post_type'      => 'post',
    'posts_per_page' => 6,
    'category_name'  => $category_slug, // dinamis dari parameter
];
$query = new WP_Query( $args );
if ( $query->have_posts() ) :
    while ( $query->have_posts() ) : $query->the_post();
        get_template_part( 'template-parts/content/content-card' );
    endwhile;
    wp_reset_postdata();
endif;
?>
```

### ✅ Kategori & Tag — Selalu fungsi WordPress

```php
<!-- Daftar kategori: BENAR -->
<?php $categories = get_categories( [ 'hide_empty' => true ] ); ?>
<?php foreach ( $categories as $cat ) : ?>
    <a href="<?php echo esc_url( get_category_link( $cat->term_id ) ); ?>">
        <?php echo esc_html( $cat->name ); ?>
    </a>
<?php endforeach; ?>
```

### ✅ Search Form — Selalu `get_search_form()`

```php
<?php get_search_form(); ?>
```

---

## Struktur Template Parts Wajib

\_tw menyediakan `template-parts/` kosong. Buat subfolder berikut dari awal:

```
theme/template-parts/
├── content/
│   ├── content-card.php        ← card artikel untuk loop (homepage, archive, search)
│   ├── content-single.php      ← konten artikel single post
│   └── content-none.php        ← jika tidak ada hasil query
├── homepage/
│   ├── hero-grid.php           ← blok hero headline (artikel utama featured)
│   ├── section-category.php    ← blok artikel per kategori (reusable, terima $args)
│   └── section-trending.php    ← blok trending/populer
├── post/
│   ├── post-meta.php           ← byline: penulis, tanggal, kategori, reading time
│   └── post-thumbnail.php      ← wrapper featured image
└── global/
    ├── site-branding.php       ← logo + nama situs
    └── social-links.php        ← ikon sosial media (opsional)
```

Cara memanggil template parts:

```php
// Panggil tanpa variabel
get_template_part( 'template-parts/homepage/hero-grid' );

// Panggil dengan variabel (WP 5.5+)
get_template_part( 'template-parts/homepage/section-category', null, [
    'category_slug' => 'teknologi',
    'title'         => 'Teknologi',
    'post_count'    => 4,
] );
```

---

## npm Scripts

Jalankan semua perintah dari folder `.workspaces/theme-src/`:

| Script           | Kapan Digunakan                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| `npm run dev`    | Build sekali saat ingin melihat hasil perubahan                           |
| `npm run watch`  | Build + watch otomatis saat aktif coding (gunakan ini selama development) |
| `npm run bundle` | Build produksi + buat zip siap upload — **jalankan di akhir saja**        |

> **Guardrail Bundling:** Output zip dari `npm run bundle` **wajib** berada di root `.workspaces/`, **bukan** di dalam folder `theme-src/`. Pastikan `package.json` sudah dikonfigurasi dengan benar untuk ini.

---

## Checklist Fase Tema (Wajib Semua ✅ Sebelum Bundle)

Sebelum menjalankan `npm run bundle`, semua item berikut **harus** sudah terpenuhi:

### Prasyarat & Konfigurasi

- [ ] `PRODUCT.md` dan `DESIGN.md` sudah dibaca dan dipatuhi secara penuh
- [ ] Nama tema di `theme/style.css` sudah diubah dari `_tw` ke nama situs dari `SITE.md`
- [ ] `functions.php` mendeklarasikan `add_theme_support('custom-logo')`, `register_nav_menus()`, dan `add_theme_support('post-thumbnails')`
- [ ] Semua nilai warna & font di `tailwind.css` sudah diambil dari `DESIGN.md`
- [ ] `npm run dev` berhasil dijalankan tanpa error

### Template & Elemen Dinamis

- [ ] **Tidak ada** link navigasi yang di-hardcode — semua memakai `wp_nav_menu()`
- [ ] **Tidak ada** `<img src="...">` hardcode untuk logo — semua memakai `the_custom_logo()`
- [ ] **Tidak ada** query artikel yang hardcode ID atau slug — semua memakai `WP_Query`
- [ ] Template parts sudah terpisah rapi di subfolder yang benar
- [ ] `front-page.php` dan `single.php` sudah dibuat mengacu pada wireframe detail di `PRODUCT.md`

### Kualitas & Kepatuhan Desain

- [ ] Skill `antislop-ui` sudah dibaca dan checklist-nya dilalui
- [ ] Tidak ada gradien default AI (biru-ungu, biru-cyan) yang tidak ada di `DESIGN.md`
- [ ] Tidak ada Tailwind CDN yang disuntikkan di `header.php` atau `functions.php`
- [ ] Semua output PHP sudah di-escape (`esc_html()`, `esc_url()`, `wp_kses_post()`)
- [ ] Tampilan sudah diuji pada viewport mobile (375px) dan desktop (1280px)

### Finalisasi & Serah Terima

- [ ] Screenshot 1200x900px homepage sudah dibuat dan disimpan sebagai `theme/screenshot.png`
- [ ] `npm run bundle` sudah dijalankan dan file `.zip` ada di root `.workspaces/`
- [ ] File `.zip` **tidak** ada di dalam folder `theme-src/`
- [ ] File `.zip` diserahkan kepada user untuk diunggah/diperbarui di WordPress
- [ ] `.workspaces/THEME_SPECS.md` sudah digenerate
- [ ] `.workspaces/PROGRESS.md` sudah diupdate dengan status "Fase Tema: SELESAI"

---

## Do's and Don'ts — Ringkasan

**WAJIB:**

- Baca `PRODUCT.md` dan `DESIGN.md` sebelum menulis satu token Tailwind pun
- Semua elemen dinamis (menu, logo, query, search) wajib pakai fungsi native WordPress sejak baris pertama
- Escape semua output PHP (`esc_html()`, `esc_url()`, `wp_kses_post()`)
- Jalankan `npm run dev` setelah setiap perubahan CSS untuk verifikasi
- Serahkan file ZIP tema kepada user setiap ada pembuatan atau perubahan tema

**DILARANG:**

- Edit `theme/style.css` atau `theme/js/` secara manual — akan ditimpa saat npm build
- Gunakan Tailwind CDN Play — \_tw menggunakan build pipeline PostCSS lokal
- Hardcode teks navigasi, URL logo, atau ID artikel dalam PHP
- Edit tema di live server via WPVibe — seluruh coding tema dilakukan **lokal**
- Mulai coding tema sebelum Hard-Gate PRD (`PRODUCT.md`) disetujui user
- Menaruh file zip output di dalam folder `theme-src/`
