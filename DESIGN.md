---
version: alpha
name: "{{ }}"
description: "{{ }}"
colors:
  primary: "{{ }}"
  secondary: "{{ }}"
  tertiary: "{{ }}"
  neutral: "{{ }}"
typography:
  h1:
    fontFamily: "{{ }}"
    fontSize: "{{ }}"
  h2:
    fontFamily: "{{ }}"
    fontSize: "{{ }}"
  body-md:
    fontFamily: "{{ }}"
    fontSize: "{{ }}"
  label-caps:
    fontFamily: "{{ }}"
    fontSize: "{{ }}"
rounded:
  sm: "{{ }}"
  md: "{{ }}"
  lg: "{{ }}"
spacing:
  sm: "{{ }}"
  md: "{{ }}"
  lg: "{{ }}"
components:
  button-primary:
    backgroundColor: "{{ }}"
    textColor: "{{ }}"
    rounded: "{{ }}"
    padding: "{{ }}"
  card-article:
    backgroundColor: "{{ }}"
    rounded: "{{ }}"
    padding: "{{ }}"
---

## Guard Condition

Cek `SITE.md` lebih dulu — jika field Identitas di sana masih placeholder kosong, berhenti dan tanyakan ke user, jangan lanjut ke file ini. Jika token di YAML front matter atau bagian di bawah masih placeholder kosong `{{ }}`, berhenti dan tanyakan ke user nilai yang dibutuhkan sebelum generate konten atau tema apa pun.

## Overview

`{{ deskripsi mood, filosofi desain, dan atmosfer visual situs — isi setelah user memberi arahan, jangan diasumsikan }}`

## Colors

`{{ penjelasan peran tiap warna: kapan primary dipakai, kapan secondary, kapan tertiary sebagai aksen interaksi, dan konteks neutral sebagai latar }}`

## Typography

`{{ penjelasan hierarki tipografi: font judul vs body, kapan label-caps dipakai, nada yang ingin dibentuk lewat pilihan font }}`

## Layout

`{{ prinsip spacing dan grid: skala spacing yang dipakai, filosofi whitespace, struktur grid homepage (hero, section kategori, trending, sidebar) }}`

## Elevation & Depth

`{{ sistem shadow/depth jika ada, hierarki surface — kosongkan jika situs flat tanpa shadow }}`

## Shapes

`{{ filosofi rounded corner: tajam/kotak vs membulat, konsistensi radius di card, button, image }}`

## Components

`{{ penjelasan tambahan di luar token: state hover/active tombol, gaya card artikel, gaya input search, dll }}`

## Do's and Don'ts

`{{ guardrail desain — hal yang wajib dan dilarang, mis. jangan pakai lebih dari 2 aksen warna, wajib kontras WCAG AA di semua tombol }}`
