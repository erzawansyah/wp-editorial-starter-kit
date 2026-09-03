# AGENTS.md

## Project Overview

Website blog niche editorial berbasis WordPress. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun di repo ini. Struktur baku: header menu kategori, homepage hero grid + block per kategori + trending, sidebar opsional, footer latest article, halaman statis, single post/page, archive kategori, search, 404.

## Tech Stack

WordPress (PHP 8.2+), classic theme + Tailwind CSS. Koneksi AI ke situs via WPVibe MCP. AI client: Antigravity.

## Agents

- **@architect** — baca SITE.md & DESIGN.md, susun rencana struktur & wireframe. Tidak menulis kode.
- **@content** — generate kategori, halaman statis, logo/favicon, draft artikel awal.
- **@engineer** — bangun tema classic + Tailwind lewat draft-safe theme builder WPVibe.
- **@qa** — audit Lighthouse, broken link, responsivitas sebelum promosi ke produksi.

## Workspace

Semua file yang dibuat oleh agent (draft, hasil generate, catatan kerja, aset sementara, output apa pun dari proses kerja) **wajib disimpan di dalam folder `.workspaces/`** di root repo, bukan di root project atau folder lain. Jangan membuat file baru di luar `.workspaces/` kecuali file tersebut memang dimaksudkan untuk jadi bagian permanen struktur repo (mis. update ke `SITE.md`, `DESIGN.md`, atau file di `.agents/skills/` dan `.agents/workflows/` yang memang sudah didefinisikan di README). Jika ragu apakah suatu file harus masuk `.workspaces/` atau tidak, tanyakan ke user lebih dulu.

## Conventions

Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/theme-structure.md` dan `content-generation.md`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.

## Boundaries (Jangan Lakukan)

- Jangan ubah wp-login atau pengaturan inti wp-admin tanpa persetujuan eksplisit.
- Jangan edit tema aktif di live langsung — semua perubahan wajib lewat draft/sandbox.
- Jangan publish, bulk-edit, atau ubah permalink tanpa approval eksplisit di chat.
- Jangan gunakan FSE block theme penuh atau page builder berat (Elementor/Divi) sebagai basis tema.
- Jangan membuat file di luar `.workspaces/` tanpa alasan yang jelas (lihat bagian Workspace).

## Definition of Done

Kategori & halaman statis terisi, draft tema disetujui, Lighthouse ≥80 (performa & SEO), tidak ada broken link, backup pra-publish terverifikasi.

## Changelog

Catat setiap pekerjaan yang selesai di repo ini. Entri terbaru di atas.

### `01. {{ YYYY-MM-DD }}`

- `{{ ringkasan singkat perubahan/pekerjaan yang selesai }}`

### `02. {{ YYYY-MM-DD }}`

- `{{ ringkasan singkat perubahan/pekerjaan yang selesai }}`
