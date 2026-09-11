---
name: wpsk-theme-craft
description: "Editorial UI craft, anti-slop, and visual design director for WordPress themes. Merges Impeccable commands (shape, critique, audit, polish, bolder, quieter, distill, typeset, colorize) with accessibility (WCAG AA/AAA contrast), mobile reflow (tap target 44px, anti-overflow), and distinctive editorial typography. Load during PRD planning (@architect), theme engineering (@engineer), and QA (@qa)."
allowed-tools: Bash(python *) Bash(python3 *) Read Write Edit Glob Grep
---

# wpsk-theme-craft

> WordPress Starter Kit Theme Craft & Visual Design Director
> Standar Baku Desain Editorial, Anti-Slop, Aksesibilitas, dan Verifikasi Deterministik

Skill ini menggabungkan seluruh keunggulan sistem **Impeccable** dengan arsitektur tema WordPress Classic + Tailwind CSS (`_tw`). Skill ini memberikan otoritas penuh kepada agen untuk bertindak layaknya seorang *Award-Winning Design Director*, menghapus segala bentuk cacat visual bawaan AI (*AI Slop*), dan memastikan tema WordPress yang dihasilkan memiliki karakter editorial yang berani, fungsional, dan nyaman dibaca.

---

## 1. Prinsip Utama & Filosofi Desain

1. **Eliminasi Total Klise AI ("Anti-Slop"):**
   * **DILARANG** menggunakan font default Inter/Arial untuk seluruh elemen tanpa diferensiasi hierarki.
   * **DILARANG** menggunakan gradien generik ungu-ke-biru (*purple-to-blue*) atau *full-page glowing orb*.
   * **DILARANG** membungkus setiap elemen ke dalam kartu (*cards*), terutama kartu di dalam kartu (*nested cards*).
   * **DILARANG** menggunakan teks abu-abu di atas latar belakang berwarna (*gray-on-color*).
   * **DILARANG** menaruh ikon kotak kecil (*rounded-square icon tile*) di atas setiap judul heading.
2. **Karakter Editorial yang Kuat (Distinctive Editorial Craft):**
   * Tipografi adalah jiwa dari situs editorial: perpaduan display font yang berkarakter dengan body text yang sangat nyaman dibaca.
   * Variasi ritme visual antar bagian: layout tidak boleh monoton (misal bukan hanya sekadar grid 3 kolom yang diulang-ulang dari atas ke bawah).
3. **Kepatuhan Terhadap Kebenaran Produk:**
   * Desain wajib patuh pada arahan identitas di `SITE.md` dan token warna/tipografi di `DESIGN.md`.

---

## 2. Kamus 9 Fungsi / Perintah Impeccable

Agen dapat memanggil atau mengeksekusi 9 mode fungsi ini sesuai tahap pengerjaan:

### A. Perencanaan & Arsitektur
* **`shape` / `craft` (Dipakai oleh `@architect` di Fase 2 PRD):**
  * Merumuskan *visual hierarchy*, kontras antar section, dan ritme tata letak di `PRODUCT.md` sebelum koding dimulai.
  * Menentukan tone editorial: apakah berkarakter *authoritative/journalistic* (tegas, serif display, garis pembatas tajam), *lifestyle/vibrant* (visual berani, warna aksen hangat), atau *minimalist/modern* (ruang negatif lega, tipografi sans modern).
  * Merancang variasi layout per kategori di frontpage (Hero grid, 3-column card, split lead-article + list, trending strip).

### B. Evaluasi & Review
* **`critique` (Dipakai untuk meninjau tata letak visual):**
  * Evaluasi kritis tingkat Design Director: apakah hierarki judul jelas? Apakah pembaca langsung tahu artikel mana yang menjadi *lead story*?
  * Memeriksa spasi: apakah grup informasi terikat erat (*tight grouping*) dan antar section memiliki pemisah yang tegas (*generous separation*)?
  * Menghapus ornamen visual tanpa fungsi (dekorasi berlebih yang hanya memperberat halaman).

### C. Audit Kualitas & Aksesibilitas
* **`audit` (Dipakai oleh `@qa` di Fase 5):**
  * **Kontras WCAG AA/AAA (Deterministik):** Validasi kontras teks normal minimal **4.5:1** dan teks besar minimal **3:1**.
    * Jalankan skrip pemeriksa kontras Python di folder skill ini:
      ```powershell
      python .agents/skills/wpsk-theme-craft/scripts/contrast-check.py "#FFFFFF" "#1E293B"
      ```
    * DILARANG mengira-ngira atau berasumsi bahwa warna kontras; wajib dihitung!
  * **Responsivitas Mobile (375px Reflow):**
    * Pastikan tidak ada horizontal scrollbar (*zero horizontal overflow*) pada viewport 375px, 768px, dan 1280px.
    * Ukuran tap target link/tombol interaktif wajib minimal **44x44px**.
  * **Ukuran Baris Baca (Body Measure):**
    * Konten artikel wajib memiliki lebar baca ideal **65–75 karakter per baris** (`max-w-prose` atau ~680–720px) agar mata pembaca tidak lelah.

### D. Penyempurnaan & Finishing
* **`polish` (Dipakai oleh `@engineer` sebelum bundling ZIP):**
  * Penyelarasan token: pastikan semua warna dan font merujuk ke token `DESIGN.md`.
  * **Browser Surfaces Styling:** Bagian yang sering dilewatkan AI wajib distyle:
    * Warna highlight seleksi teks: `selection:bg-primary selection:text-white` (sesuai palet).
    * Focus ring aksesibilitas: `focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent`.
    * Kustomisasi kursor input dan scrollbar jika relevan.
  * Status interaktif lengkap: pastikan setiap tombol dan link memiliki status `:hover`, `:active`, `:focus-visible`, dan `:disabled`.

### E. Modifiers Penyetelan Cepat (Quick Tuning)
Gunakan modifier ini jika user memberikan feedback revisi visual tertentu:
* **`bolder` (Jika desain dirasa kaku, datar, atau membosankan):**
  * Naikkan rasio skala tipografi (misal perbesar judul hero ke `text-4xl md:text-5xl lg:text-6xl font-black`).
  * Tajamkan kontras warna aksen dari `DESIGN.md`.
  * Berikan depth yang nyata (bayangan berbobot dengan blur halus atau border kontras 1-2px).
* **`quieter` (Jika desain dirasa terlalu ramai, norak, atau melelahkan):**
  * Redam saturasi warna latar, gunakan off-white hangat atau tint abu-abu netral.
  * Perbesar whitespace (padding vertikal antar section).
  * Kembalikan panggung visual ke teks bacaan dan featured media.
* **`distill` (Pangkas ke esensi minimalis):**
  * Hapus border kartu yang tidak perlu; gunakan whitespace sebagai pemisah.
  * Hilangkan ornamen/ikon dekoratif yang tidak menyampaikan informasi.
* **`typeset` (Koreksi tipografi editorial):**
  * Pastikan line-height proporsional: heading rapat (`leading-tight` atau `leading-[1.15]`), body text lega (`leading-relaxed` atau `leading-[1.7]`).
  * Display font berukuran besar di atas 32px diberi tracking negatif halus (`tracking-tight` atau `-0.02em`).
* **`colorize` (Penyelarasan palet warna):**
  * Dilarang menggunakan pure black `#000000` pekat untuk teks; gunakan tinted slate/zinc/neutral gelap (`#0F172A`, `#18181B`, `#111827`).
  * Berikan tint halus pada warna background sekunder (jangan abu-abu mati).

---

## 3. The Craft Floor (Standar Kualitas Mutlak)

Sebelum file ZIP tema diserahkan atau commit dilakukan, periksa checklist Craft Floor berikut:

| Kriteria | Standar Wajib | Cara Verifikasi |
| :--- | :--- | :--- |
| **Kontras Teks** | Normal: ≥4.5:1, Large: ≥3:1 | Jalankan `contrast-check.py` |
| **Lebar Baca (Measure)** | 65–75 karakter per baris pada single post | Cek class `max-w-prose` (~65ch) pada `.entry-content` |
| **Ritme Vertikal Spacing** | Spasi di atas heading selalu > spasi di bawah heading | Spasi atas `mt-8` / `mt-10`, spasi bawah `mb-3` / `mb-4` |
| **Tap Target Mobile** | Area klik tombol / navigasi minimal 44x44px | Cek padding `py-2.5 px-4` atau `min-h-[44px]` |
| **Anti-Overflow Layar** | Tidak ada pergeseran horizontal di 375px | Uji di browser viewport 375px |
| **Browser Surfaces** | Styling `::selection` dan `:focus-visible` aktif | Cek class global di CSS tema |
| **Larangan Kartu Bersarang** | Tidak ada card di dalam card | Inspeksi struktur HTML |
| **Kontainer Logo Header** | Logo dikunci `max-h-12 md:max-h-14 w-auto object-contain` | Inspeksi header saat logo gambar diunggah |

---

## 4. Integrasi Verifikasi Visual Playwright (Fase QA)

Pada Fase 5 (QA), agen `@qa` tidak boleh hanya menduga-duga tampilan situs secara teoritis. Agen **WAJIB memanfaatkan browser Playwright bawaan** untuk mengambil bukti visual riil:

1. Buka URL halaman target (Homepage, Single Post, Category Archive) di background.
2. Atur viewport ke ukuran standar:
   * **Desktop:** Lebar 1440px x Tinggi 900px.
   * **Mobile:** Lebar 375px x Tinggi 812px.
3. Ambil **Full-Page Screenshot** (`browser_take_screenshot` dengan parameter full page).
4. Sematkan gambar hasil tangkapan layar langsung ke dalam dokumen **Artifact** di Antigravity agar user dapat melihat bukti visualnya secara instan tanpa perlu membuka browser secara manual.
