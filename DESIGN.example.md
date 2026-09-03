---
version: alpha
name: "BeritaFoodies"
description: "Portal kuliner editorial Indonesia — berita restoran, resep, dan gaya hidup makanan."
colors:
  primary: "#D94F3D"
  secondary: "#1A1A2E"
  tertiary: "#F4A823"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: "Playfair Display"
    fontSize: "48px"
  h2:
    fontFamily: "Playfair Display"
    fontSize: "32px"
  body-md:
    fontFamily: "Inter"
    fontSize: "16px"
  label-caps:
    fontFamily: "Inter"
    fontSize: "11px"
rounded:
  sm: "2px"
  md: "4px"
  lg: "8px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
components:
  button-primary:
    backgroundColor: "#D94F3D"
    textColor: "#FFFFFF"
    rounded: "2px"
    padding: "10px 20px"
  card-article:
    backgroundColor: "#FFFFFF"
    rounded: "4px"
    padding: "0px"
---

## Guard Condition

Cek `SITE.md` lebih dulu — jika field Identitas di sana masih placeholder kosong, berhenti dan tanyakan ke user, jangan lanjut ke file ini. Jika token di YAML front matter atau bagian di bawah masih placeholder kosong `{{ }}`, berhenti dan tanyakan ke user nilai yang dibutuhkan sebelum generate konten atau tema apa pun.

## Overview

Portal kuliner dengan karakter editorial yang tegas — seperti majalah cetak yang digitalisasi. Mood-nya hangat tapi tidak informal: pembaca merasa sedang membaca rekomendasi dari editor yang tahu betul soal makanan, bukan sekadar agregator konten. Warna merah primer memberi energi dan selera; latar netral krem memberi ruang napas agar konten tidak sesak.

## Colors

- **Primary `#D94F3D`** — merah cabe yang hangat. Dipakai untuk aksen utama: link aktif, badge kategori, tombol CTA, underline judul seksi.
- **Secondary `#1A1A2E`** — hampir hitam, untuk teks body dan heading utama. Kontras tinggi di latar krem.
- **Tertiary `#F4A823`** — kuning kunyit. Aksen interaksi (hover state, tag trending, highlight kutipan). Pakai hemat — maksimal 2 elemen per halaman.
- **Neutral `#F7F5F2`** — krem putih sebagai background utama. Lebih hangat dari putih murni, cocok dengan tone editorial.

## Typography

Hierarki dua-font yang kontras: **Playfair Display** (serif) untuk semua heading — memberi kesan editorial, berotoritas. **Inter** (sans-serif) untuk body dan label — bersih, mudah dibaca di layar kecil.

- **H1 (48px):** Hero headline homepage. Hanya satu per halaman.
- **H2 (32px):** Judul seksi (per kategori di homepage, judul artikel di single post).
- **Body-md (16px / line-height 1.7):** Teks artikel. Jarak baris longgar untuk kenyamanan baca panjang.
- **Label-caps (11px, uppercase, letter-spacing 0.08em):** Tag kategori, keterangan foto, metadata (penulis, tanggal). Jangan pakai untuk teks panjang.

## Layout

Grid 12-kolom. Homepage dibagi tiga zona:
1. **Hero:** full-width atau 8+4, artikel utama terbesar dengan gambar dominan.
2. **Kategori blocks:** 3-kolom card grid per seksi. Setiap seksi punya label kategori di atas, link "Lihat Semua" di kanan.
3. **Trending sidebar:** 4-kolom di desktop (jika sidebar aktif), full-width di mobile — daftar judul sederhana dengan nomor urut.

Spacing konsisten: gutter 16px, padding seksi 32px vertikal, margin antar blok 48px.

## Elevation & Depth

Desain flat dengan satu pengecualian: card artikel mendapat `box-shadow: 0 1px 3px rgba(0,0,0,0.08)` — hanya terasa saat di-hover (`0 4px 12px rgba(0,0,0,0.12)`). Tidak ada shadow dekoratif. Kedalaman visual hanya dari kontras warna dan whitespace.

## Shapes

Sudut kotak (`rounded: sm 2px`). Karakter majalah — tajam dan bersih. Card artikel tidak membulat. Tombol sedikit membulat di 2px agar tidak terasa terlalu kaku. Gambar artikel: kotak sempurna (no border-radius).

## Components

- **Card artikel:** Gambar di atas (aspect-ratio 16:9), label kategori (label-caps, primary color) di bawah gambar, judul (H3 atau H4 tergantung ukuran card), byline. Tidak ada padding di gambar, padding konten 12px.
- **Button primary:** Solid merah, teks putih, hover gelap 10% (`#C2443A`). Jangan pakai outline variant sebagai CTA utama.
- **Input search:** Border 1px solid `#D0CDC9`, focus border primary. Placeholder teks secondary dengan opacity 50%.
- **Kategori badge/tag:** Background primary dengan opacity 10%, teks primary. Hover: background solid primary, teks putih.

## Do's and Don'ts

**Wajib:**
- Kontras teks minimal WCAG AA di semua kondisi (body di latar krem sudah aman, cek label kecil di background berwarna).
- Gambar artikel wajib punya `alt` deskriptif — ini portal editorial, bukan portofolio.
- Konsistensi aspect ratio gambar di setiap level (hero 21:9, card 16:9, thumbnail 4:3).

**Dilarang:**
- Lebih dari 2 warna aksen dalam satu halaman (primary + salah satu dari tertiary atau warna kategori).
- Font lebih dari 2 family. Jangan tambahkan font dekoratif ketiga.
- Animasi yang menggerakkan konten lebih dari 4px — ini bukan landing page produk.
- Background hitam penuh atau gradien gelap dramatis — bertentangan dengan tone editorial hangat.
