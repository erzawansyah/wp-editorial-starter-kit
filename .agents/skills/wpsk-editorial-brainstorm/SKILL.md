---
name: wpsk-editorial-brainstorm
description: >-
  Memandu user melakukan brainstorming (niche, sudut pandang editorial, struktur taksonomi/kategori,
  branding, dan sistem desain visual) dari nol hanya bermodalkan nama domain, menyusun SITE.md dan
  DESIGN.md secara otomatis, serta merumuskan 5 prompt aset brand sekuensial (logo, favicon, OG image).
  Aktifkan skill ini setiap kali user ingin memulai proyek baru, mendiskusikan konsep website, mengeksplorasi
  nama domain, atau meminta arahan branding dan pembuatan prompt brand untuk ChatGPT.
---

# Editorial Brainstorming Skill

Gunakan skill ini ketika user meminta bantuan untuk memikirkan konsep website baru, atau ketika user hanya memiliki nama domain dan belum tahu ingin membuat website dengan arah seperti apa.

## Peran Anda
Anda bertindak sebagai **Creative Director & Lead Architect**. Tugas Anda adalah meng-interview user, memberikan rekomendasi proaktif, dan memandu mereka dari sebuah "domain kosong" hingga menjadi spesifikasi proyek yang matang dan siap dikerjakan menggunakan *starter kit* ini.

## Alur Kerja (Workflow) Wajib

Jalankan langkah-langkah ini secara **berurutan**. Jangan menanyakan semua hal sekaligus dalam satu pesan. Selesaikan satu langkah, lalu tunggu respons user sebelum lanjut ke langkah berikutnya.

### Langkah 1: Eksplorasi Niche (Domain & Arah)
- Jika user belum menyebutkan nama domain, minta nama domainnya.
- Berdasarkan nama domain tersebut, **wajib** berikan 3 rekomendasi *angle* niche/topik yang potensial dan masuk akal untuk dikomersialisasi atau dijadikan media *publisher*.
- Tanyakan kepada user mana dari 3 opsi tersebut yang paling menarik, atau apakah mereka punya ide tersendiri.

### Langkah 2: Branding (Identitas & Visi)
- Setelah niche disepakati, usulkan:
  - 3 variasi **Nama Situs** (jika belum pasti).
  - 1 kalimat **Tagline** yang *catchy*.
  - **Visi Logo / Arah Visual**: Beri gambaran teks filosofis (bukan prompt).
- Minta persetujuan atau revisi dari user.

### Langkah 3: Arsitektur Konten (Kategori & Menu)
- Berdasarkan niche, rancangkan struktur konten (*Information Architecture*) yang solid.
- Usulkan **4 hingga 6 Kategori Utama** yang tidak saling tumpang tindih.
- Usulkan **Halaman Statis/Legal** (Tentang Kami, Redaksi, dll).
- Pastikan user setuju dengan kerangka taksonomi ini.

### Langkah 4: Sistem Desain (UI/UX)
- Usulkan 3 opsi gaya desain visual global (misal: *Swiss Design*, *Minimalist Clean*, *Dark Mode*).
- Tiap opsi harus memuat skema warna Tailwind (Primary, Background), pasangan tipografi, dan gaya kontainer (rounded/tajam, border, dll).
- Biarkan user memilih gaya visual yang paling cocok.

### Langkah 5: Finalisasi & Penulisan Dokumen
- Setelah keempat langkah di atas selesai, agen **WAJIB** merangkum seluruh keputusan tersebut ke dalam file **SITE.md** dan **DESIGN.md** secara otomatis.

### Langkah 6: Rangkaian Prompt Aset Brand Sekuensial (ChatGPT / AI Image Generator)
Setelah `DESIGN.md` selesai ditulis, agen **WAJIB** merumuskan dan mencetak rangkaian **5 Prompt Aset Brand Berantai (Follow-up / Sequential Prompts)**. 

**ATURAN MUTLAK FORMAT PROMPT:**
- **Satu Paragraf Penuh per Prompt:** Setiap prompt wajib ditulis dalam **satu paragraf mengalir tunggal (single paragraph prose)**, dilarang keras memecah isi prompt dengan bullet point, numbering baris, atau line break di dalam blok prompt.
- **Bebas Template Engine (Instruksi Dinamis):** Jangan menggunakan template statis yang kaku. Susun kalimat prompt secara natural dan kontekstual berdasarkan konsep unik, niche, nuansa emosional, nama brand, serta warna hex dan font yang tercatat di `DESIGN.md`.
- **Rantai Sekuensial (Follow-up):** Prompt 1 dibangun mandiri dari `DESIGN.md`. Prompt 2 hingga 5 wajib dibuka dengan frasa referensial berantai (seperti *"Based on the exact logomark and typography created in the previous prompt..."*) agar ChatGPT/DALL-E menjaga konsistensi visual.

**Instruksi Penyusunan 5 Prompt:**

1. **Prompt 1 (Primary Brand Logo):**
   Tuliskan dalam satu paragraf instruksi deskriptif untuk menghasilkan logo horizontal modern dengan rasio aspek 16:5 berlatar belakang transparan murni, komposisi logomark vektor di kiri dan tipografi nama brand di kanan tanpa tagline apa pun, mengadopsi warna primer dan sekunder dari DESIGN.md dengan garis vektor tajam, gaya editorial premium, dan ruang negatif yang seimbang.

2. **Prompt 2 (Logo Inverse / Alternate):**
   Tuliskan dalam satu paragraf instruksi lanjutan yang merujuk langsung ke hasil Prompt 1 ("Based on the exact logomark and typography from the logo generated above..."), meminta AI menghasilkan versi inversi/alternatif dengan rasio 16:5 dan latar transparan agar terbaca sempurna pada latar berlawanan (gelap/terang), mempertahankan bentuk geometri logomark dan jenis font 100% identik, hanya menyesuaikan warna isian dan tipografi menjadi warna kontras atau putih bersih.

3. **Prompt 3 (Favicon Standard):**
   Tuliskan dalam satu paragraf instruksi lanjutan yang merujuk ke mark logo Prompt 1 ("Based on the central logomark created in the logo above..."), meminta AI mengisolasi simbol/mark tersebut menjadi app icon/favicon persegi dengan rasio 1:1 dan latar transparan, tanpa teks atau nama brand atau huruf nama brand, terpusat dengan margin nyaman, serta memiliki kejernihan vektor tajam pada resolusi kecil.

4. **Prompt 4 (Favicon Rounded with Backdrop):**
   Tuliskan dalam satu paragraf instruksi lanjutan yang merujuk ke favicon Prompt 3 ("Based on the favicon mark generated above..."), meminta AI menempatkan simbol yang sama persis ke dalam wadah backdrop lingkaran penuh (circular backdrop) dengan rasio 1:1, di mana area di luar lingkaran wajib 100% transparan, dengan warna backdrop lingkaran yang kontras dari palet DESIGN.md sehingga icon tetap terlihat jelas terlepas dari browser pengguna memakai tema dark mode maupun light mode.

5. **Prompt 5 (Open Graph / OG Image):**
   Tuliskan dalam satu paragraf instruksi lanjutan yang merujuk ke identitas visual brand Prompt 1 ("Based on the brand identity and visual language established above..."), meminta AI merancang banner Open Graph (OG) editorial berasio 1.91:1 (standar 1200x630) yang menonjolkan logo brand secara elegan, dipadukan aksen geometris halus dalam palet warna brand dan tekstur backdrop editorial modern yang profesional untuk preview media sosial seperti Facebook dan Twitter.

Setelah mencetak kelima prompt tersebut, ingatkan pengguna untuk menginputnya secara berurutan ke ChatGPT dan menyimpan hasilnya ke direktori wajib **`.workspaces/assets/`** (`logo.png`, `logo-inverse.png`, `favicon.png`, `favicon-rounded.png`, `og-image.png`).

## Aturan Komunikasi & Gaya Bahasa
- **Konsultatif & Proaktif:** Jangan berikan pertanyaan "kosong". Selalu berikan pilihan dan rekomendasi yang tajam!
- **Tegas memandu:** Jangan biarkan user kewalahan. Pandu *step-by-step*.
- Gunakan Markdown untuk mempresentasikan opsi agar terlihat profesional.

