---
# Sistem desain untuk website ini. Isi sebelum memanggil AI untuk fase tema.
# Lihat DESIGN.example.md untuk contoh yang sudah terisi penuh.
version: alpha
name: "{{ nama website }}"
description: "{{ satu kalimat deskripsi niche dan karakter website }}"
colors:
  primary: "{{ hex — warna utama, aksen & CTA }}"
  secondary: "{{ hex — warna teks & heading }}"
  tertiary: "{{ hex — aksen interaksi, hover state, badge trending }}"
  neutral: "{{ hex — warna latar belakang utama }}"
typography:
  h1:
    fontFamily: "{{ nama font, misal: Playfair Display }}"
    fontSize: "{{ misal: 48px }}"
  h2:
    fontFamily: "{{ nama font }}"
    fontSize: "{{ misal: 32px }}"
  body-md:
    fontFamily: "{{ nama font, misal: Inter }}"
    fontSize: "{{ misal: 16px }}"
  label-caps:
    fontFamily: "{{ nama font }}"
    fontSize: "{{ misal: 11px — untuk tag, metadata, byline }}"
rounded:
  sm: "{{ misal: 2px — untuk elemen tajam }}"
  md: "{{ misal: 4px }}"
  lg: "{{ misal: 8px — untuk modal atau card besar }}"
spacing:
  sm: "{{ misal: 8px }}"
  md: "{{ misal: 16px }}"
  lg: "{{ misal: 32px }}"
components:
  button-primary:
    backgroundColor: "{{ hex — gunakan primary atau variannya }}"
    textColor: "{{ hex — pastikan kontras WCAG AA }}"
    rounded: "{{ misal: 2px }}"
    padding: "{{ misal: 10px 20px }}"
  card-article:
    backgroundColor: "{{ hex — biasanya putih atau neutral }}"
    rounded: "{{ misal: 4px }}"
    padding: "{{ misal: 0px — jika gambar flush ke tepi card }}"
---

## Guard Condition

Cek `SITE.md` lebih dulu — jika field Identitas di sana masih placeholder kosong, berhenti dan tanyakan ke user, jangan lanjut ke file ini. Jika token di YAML front matter atau bagian di bawah masih placeholder kosong `{{ }}`, berhenti dan tanyakan ke user nilai yang dibutuhkan sebelum generate konten atau tema apa pun.

## Overview

`{{ Deskripsikan mood, filosofi desain, dan atmosfer visual situs. Contoh: "Portal berita dengan karakter editorial yang tegas — seperti majalah cetak yang digitalisasi. Warna hangat, bukan informal." Isi setelah user memberi arahan, jangan diasumsikan. }}`

## Colors

`{{ Jelaskan peran tiap warna: kapan primary dipakai, kapan secondary, kapan tertiary sebagai aksen interaksi, dan konteks neutral sebagai latar. Sertakan juga catatan kontras WCAG jika ada warna yang perlu diwaspadai. }}`

## Typography

`{{ Jelaskan hierarki tipografi: font judul vs body, kapan label-caps dipakai, nada yang ingin dibentuk lewat pilihan font. Contoh: "Playfair Display untuk heading memberi kesan editorial; Inter untuk body menjamin keterbacaan di layar kecil." }}`

## Layout

`{{ Jelaskan prinsip spacing dan grid: skala spacing yang dipakai, filosofi whitespace, struktur grid homepage (hero, section kategori, trending, sidebar). Sebutkan jumlah kolom dan breakpoint utama jika spesifik. }}`

## Elevation & Depth

`{{ Jelaskan sistem shadow/depth jika ada, hierarki surface. Kosongkan bagian ini dengan catatan "flat design, tidak ada shadow" jika memang tidak digunakan. }}`

## Shapes

`{{ Jelaskan filosofi rounded corner: tajam/kotak vs membulat, konsistensi radius di card, button, dan image. }}`

## Components

`{{ Jelaskan detail komponen di luar token YAML: state hover/active tombol, gaya card artikel (gambar flush atau padding), gaya input search, dsb. }}`

## Do's and Don'ts

`{{ Tulis guardrail desain yang spesifik: hal yang wajib dan dilarang. Contoh: "Wajib kontras WCAG AA di semua tombol. Jangan pakai lebih dari 2 aksen warna dalam satu halaman." }}`
