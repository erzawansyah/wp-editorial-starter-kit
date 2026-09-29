---
name: theme-guardrails
description: 8 aturan baku teknis tema WordPress Classic + Tailwind CSS (_tw), proteksi logo anti-meluap, dynamic frontpage category section, template singular page, single post, author archive, dan pipeline PostCSS lokal.
trigger: always_on
---

# Theme Engineering Guardrails & Technical Standards

Standar baku teknis untuk arsitektur tema WordPress Classic + Tailwind CSS (`_tw`) di `.workspaces/theme-src/`. Wajib dipatuhi oleh `@engineer`.

---

## 1. 8 Aturan Baku Teknis Tema

1. **Header & Container Logo (Anti-Meluap):**
   - Container logo **wajib** dikunci dengan kelas Tailwind:
     `max-h-12 md:max-h-14 w-auto object-contain flex-shrink-0`
   - Aktifkan `add_theme_support('custom-logo')`.
   - Header harus tampil rapi baik saat menggunakan Site Title teks maupun Logo gambar, tanpa pernah meluap dari navbar.

2. **Navigasi Dinamis:**
   - Dilarang keras melakukan hardcode pada link menu navbar atau footer. Wajib menggunakan `wp_nav_menu()` dengan registrasi `theme_location` yang sesuai.

3. **Frontpage Dinamis & Terkonfigurasi (Anti-Hardcode Kategori):**
   - `front-page.php` wajib menampilkan variasi section per kategori sesuai `PRODUCT.md`.
   - **DILARANG KERAS MENG-HARDCODE SLUG ATAU ID KATEGORI.**
   - Tema wajib menyediakan antarmuka konfigurasi (Theme Customizer via Customizer API atau Theme Options Page) untuk memilih kategori yang ditampilkan pada tiap section, beserta judul (*title*) dan subjudul (*subtitle*) kustom.
   - **Fallback Dinamis Otomatis:** Jika kategori belum dipilih di Customizer atau kategori terhapus/diubah oleh pengguna, tema wajib otomatis mengambil kategori yang tersedia secara berurutan (`get_categories(['hide_empty' => true])`) agar layout homepage tidak pernah kosong atau rusak.
   - Bagian bawah frontpage wajib memiliki navigasi/tombol pagination *"Lihat Artikel Lainnya"* yang mengarah langsung ke Archive Page spesifik.

4. **Single Post Lengkap (`single.php`):**
   - **Social Share Buttons:** Wajib menyediakan minimal 6 kanal berbagi: WhatsApp, Telegram, Facebook, X/Twitter, Threads, dan Copy Link dengan feedback visual status tersalin.
   - **Author Box:** Wajib memuat avatar (`get_avatar()`), nama, biografi singkat, dan link arsip penulis.
   - **Comment Box:** Wajib ter-styling penuh menggunakan utilitas Tailwind CSS (bukan form mentah default WordPress).
   - **Custom Sidebar Komponen:** Sidebar tersusun dari komponen PHP terpisah (bukan dynamic widget bawaan WP yang tidak terkontrol styling-nya).

5. **Author Archive Wajib (`author.php`):**
   - File template `author.php` wajib disediakan.
   - Memuat profil header lengkap penulis (avatar besar, nama display, biografi, jumlah artikel terbit) dan grid arsip artikel yang ditulis oleh author tersebut.

6. **Template Singular Page Anti-Polos (`page.php`):**
   - Template singular page untuk post type `page` **dilarang dibuat polos/kotak kosong**.
   - Wajib memiliki hero page header yang ter-styling elegan (breadcrumb, heading font berukuran display, excerpt/subtitle jika ada).
   - Wadah featured media sinematik dengan aspect ratio terukur.
   - Tipografi Gutenberg yang tertata rapi (`prose prose-lg max-w-4xl mx-auto`).

7. **Query & Taksonomi Dinamis:**
   - Selalu gunakan `WP_Query` dengan parameter `paged`, `posts_per_page`, dan sanitasi taksonomi yang tepat. Dilarang query menggunakan ID atau slug statis hardcoded.

8. **Tanpa Tailwind CDN (PostCSS Pipeline):**
   - Build tema wajib melalui pipeline PostCSS lokal (`npm run dev` / `npm run bundle`).
   - Dilarang menyematkan script Tailwind CDN (`cdn.tailwindcss.com`).

---

## 2. Manajemen Direktori & Artefak Tema

- **Lokasi Pengerjaan:** Seluruh source code tema berada di `.workspaces/theme-src/`.
- **Generated Assets:** Dilarang mengedit manual `theme/style.css` dan `theme/js/`.
- **Bundle Output:** Ekspor tema ZIP dari `npm run bundle` **wajib diletakkan di root `.workspaces/`** (contoh: `.workspaces/<slug-tema>.zip`), bukan tersembunyi di subfolder `theme-src/`.
- **Dokumentasi Handover:** Generate `.workspaces/THEME_SPECS.md` setelah bundling tema selesai.
