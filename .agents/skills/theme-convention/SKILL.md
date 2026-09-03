---
# Skill: Theme Convention
name: theme-convention
description: >
  Konvensi struktur tema WordPress classic + Tailwind CSS untuk starter kit
  editorial ini. Gunakan saat fase tema dimulai (@engineer). Semua keputusan
  struktur dan penamaan file mengacu ke dokumen ini — jangan improvisasi.
---

# Theme Convention

## Stack

- **WordPress Classic Theme** (bukan Block Theme / FSE)
- **Tailwind CSS** via CDN Play untuk development cepat, atau via `npm` + build step untuk produksi
- **PHP 8.2+**
- Tidak menggunakan page builder (Elementor, Divi, dsb.)

---

## Struktur Folder Tema

```
themes/
└── {slug-tema}/               ← nama tema = slug dari SITE.md, lowercase, dash
    ├── style.css              ← header tema WordPress (wajib)
    ├── functions.php          ← enqueue, register, hooks
    ├── index.php              ← fallback template
    ├── front-page.php         ← homepage (editorial grid)
    ├── single.php             ← single post
    ├── page.php               ← single page
    ├── archive.php            ← archive kategori
    ├── search.php             ← halaman search
    ├── 404.php                ← halaman not found
    ├── sidebar.php            ← sidebar (jika diaktifkan)
    ├── screenshot.png         ← preview tema 1200×900px
    ├── assets/
    │   ├── css/
    │   │   └── main.css       ← output Tailwind (jika build step)
    │   ├── js/
    │   │   └── main.js        ← minimal JS, tanpa framework berat
    │   └── images/
    │       └── logo.svg
    └── template-parts/
        ├── header/
        │   ├── site-header.php       ← header utama
        │   └── nav-primary.php      ← navigasi kategori
        ├── footer/
        │   ├── site-footer.php       ← footer utama
        │   └── footer-latest.php    ← widget latest article di footer
        ├── homepage/
        │   ├── hero-grid.php         ← blok hero/headline atas
        │   ├── section-category.php  ← blok artikel per kategori (reusable)
        │   └── section-trending.php  ← blok trending
        ├── post/
        │   ├── card-article.php      ← card artikel (reusable, pakai di mana saja)
        │   ├── post-meta.php         ← byline: penulis, tanggal, kategori
        │   └── post-thumbnail.php    ← wrapper gambar artikel
        └── global/
            ├── breadcrumb.php
            ├── pagination.php
            └── search-form.php
```

---

## Penamaan Konvensi

| Konteks | Format | Contoh |
|---|---|---|
| Slug tema | `kebab-case` | `berita-foodies` |
| File PHP template | `kebab-case.php` | `front-page.php` |
| File template-parts | `kebab-case.php` | `card-article.php` |
| Class Tailwind custom | Hindari — pakai utility langsung | — |
| ID HTML | `kebab-case` | `site-header`, `hero-grid` |
| Class HTML komponen | `prefix-nama` | `card-article`, `nav-primary` |

---

## Template Parts — Cara Pemanggilan

Selalu gunakan `get_template_part()` dengan path relatif dari root tema:

```php
// Benar
get_template_part('template-parts/post/card-article');

// Salah — jangan pakai include/require langsung
include 'template-parts/post/card-article.php';
```

Untuk passing variabel ke template-part (WordPress 5.5+):

```php
get_template_part('template-parts/post/card-article', null, [
    'post_id' => get_the_ID(),
    'show_excerpt' => true,
]);
```

---

## Tailwind CSS

### Development (CDN Play)
Gunakan CDN Play untuk iterasi cepat saat build bersama WPVibe:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

Tambahkan konfigurasi tema inline setelah CDN:

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: '#D94F3D',    // dari DESIGN.md
          secondary: '#1A1A2E',
          tertiary: '#F4A823',
          neutral: '#F7F5F2',
        },
        fontFamily: {
          heading: ['"Playfair Display"', 'serif'],
          body: ['Inter', 'sans-serif'],
        },
      }
    }
  }
</script>
```

> **Catatan:** Nilai warna dan font harus diambil dari `DESIGN.md`, bukan di-hardcode manual.

### Produksi (Build Step)
Sebelum deploy ke produksi, ganti CDN dengan build file:
1. `npm init` di folder tema
2. Install `tailwindcss`
3. Jalankan purge/build untuk menghapus class yang tidak dipakai
4. Output ke `assets/css/main.css`

---

## functions.php — Struktur Dasar

```php
<?php
// Enqueue styles & scripts
function theme_enqueue_assets() {
    wp_enqueue_style('theme-style', get_stylesheet_uri(), [], '1.0.0');
    // Enqueue main.css jika sudah build
    // wp_enqueue_script('theme-main', get_template_directory_uri() . '/assets/js/main.js', [], '1.0.0', true);
}
add_action('wp_enqueue_scripts', 'theme_enqueue_assets');

// Theme support
function theme_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'gallery', 'caption']);
    add_theme_support('custom-logo');

    // Register menus
    register_nav_menus([
        'primary' => 'Menu Utama (Kategori)',
        'footer'  => 'Menu Footer',
    ]);

    // Register sidebar (jika dipakai)
    register_sidebar([
        'name'          => 'Sidebar Utama',
        'id'            => 'sidebar-main',
        'before_widget' => '<div class="widget mb-8">',
        'after_widget'  => '</div>',
        'before_title'  => '<h3 class="widget-title font-heading text-sm uppercase tracking-widest mb-4">',
        'after_title'   => '</h3>',
    ]);
}
add_action('after_setup_theme', 'theme_setup');
```

---

## Halaman yang Wajib Ada

| Template | File | Keterangan |
|---|---|---|
| Homepage editorial | `front-page.php` | Hero grid + section kategori + trending |
| Single post | `single.php` | Artikel dengan post-meta, thumbnail, konten |
| Single page | `page.php` | Halaman statis (Tentang Kami, dsb.) |
| Archive kategori | `archive.php` | Grid artikel per kategori |
| Search results | `search.php` | Form + hasil pencarian |
| 404 | `404.php` | Pesan error + link ke homepage |

---

## Do's and Don'ts Tema

**Wajib:**
- Semua output yang mungkin berisi input user wajib di-escape (`esc_html()`, `esc_url()`, `esc_attr()`, `wp_kses_post()`)
- Gunakan `get_template_directory_uri()` untuk path aset, bukan path hardcode
- Semua string UI wajib wrapped dalam `__()` atau `esc_html__()` untuk i18n

**Dilarang:**
- Jangan masukkan logika bisnis ke template — pindahkan ke `functions.php` atau custom class
- Jangan query database langsung di template — gunakan `WP_Query`
- Jangan edit tema langsung di live (via wp-admin Theme Editor) — semua perubahan via WPVibe draft
