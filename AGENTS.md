# AGENTS.md

## Project Overview

Repo ini adalah **Starter Kit** untuk produksi massal website niche blog/editorial berbasis WordPress. Setiap proyek baru dimulai dengan meng-clone repo ini, mengisi `SITE.md` dan `DESIGN.md`, lalu menjalankan workflow di bawah. Baca `SITE.md` lalu `DESIGN.md` sebelum mengerjakan apa pun.

Struktur baku setiap website yang dihasilkan: header menu kategori, homepage hero grid + block per kategori + trending, sidebar opsional, footer latest article, halaman statis, single post/page, archive kategori, search, 404.

## Tech Stack

WordPress (PHP 8.2+), classic theme + Tailwind CSS. Koneksi AI ke situs via WPVibe MCP. AI client: Antigravity.

## Agents

- **@architect** — baca SITE.md & DESIGN.md, susun rencana struktur & wireframe. Tidak menulis kode.
- **@content** — generate kategori, halaman statis, logo/favicon, draft artikel awal.
- **@engineer** — bangun tema classic + Tailwind lewat draft-safe theme builder WPVibe.
- **@qa** — audit Lighthouse, broken link, responsivitas sebelum promosi ke produksi.

## Standard Operating Procedure (SOP)

Urutan kerja wajib diikuti secara berurutan. Jangan loncat fase.

1. **Setup (Manusia):** Clone repo ini, install WordPress di server, setup plugin dan tema dasar.
2. **Briefing (Manusia):** Isi `SITE.md` (identitas website) dan `DESIGN.md` (sistem desain).
3. **Fase Konten (@content):** Generate kategori, halaman statis (Tim Redaksi, Tentang Kami, Kebijakan Privasi, dll.), logo, favicon, dan draft artikel awal.
4. **Fase Tema (@architect → @engineer):** Architect menyusun wireframe berdasarkan DESIGN.md, lalu engineer membangun tema (layout editorial, header, footer, template standar).
5. **Fase QA (@qa):** Audit Lighthouse ≥80 (performa & SEO), broken link check, uji responsivitas.
6. **Deployment (Manusia):** Promosi ke environment produksi setelah approval.

## Workspace

Semua file yang dibuat oleh agent (draft, hasil generate, catatan kerja, aset sementara, output apa pun dari proses kerja) **wajib disimpan di dalam folder `.workspaces/`** di root repo, bukan di root project atau folder lain. Jangan membuat file baru di luar `.workspaces/` kecuali file tersebut memang dimaksudkan untuk jadi bagian permanen struktur repo (mis. update ke `SITE.md`, `DESIGN.md`, atau file di `.agents/skills/`). Jika ragu apakah suatu file harus masuk `.workspaces/` atau tidak, tanyakan ke user lebih dulu.

## Conventions

Struktur file tema, penamaan template-parts, dan konvensi konten mengikuti `.agents/skills/`. Jangan improvisasi struktur baru tanpa mencatat alasannya di `DESIGN.md`. Bahasa konten default: Indonesia, gaya editorial.

## WPVibe MCP

WPVibe MCP bisa terhubung ke banyak situs WordPress sekaligus. Untuk mencegah kesalahan target, ikuti aturan berikut:

1. **Baca field URL di `SITE.md` terlebih dahulu.** Nilai URL tersebut adalah satu-satunya situs yang boleh dioperasikan dalam sesi kerja ini.
2. **Jika field URL masih placeholder `{{ }}`**, jangan lakukan operasi WPVibe apa pun. Pandu user untuk:
   - Mengisi URL situs target di `SITE.md`.
   - Memastikan situs tersebut sudah terhubung ke WPVibe (plugin WPVibe terinstall dan aktif di WordPress target).
3. **Jika URL sudah terisi**, validasi bahwa situs tersebut merespons melalui WPVibe sebelum menjalankan operasi pertama. Setelah tervalidasi, fokus sepenuhnya ke situs itu — jangan query, jangan manipulasi, jangan sentuh situs lain yang mungkin juga terhubung ke WPVibe.

## Boundaries (Jangan Lakukan)

- Jangan ubah wp-login atau pengaturan inti wp-admin tanpa persetujuan eksplisit.
- Jangan edit tema aktif di live langsung — semua perubahan wajib lewat draft/sandbox.
- Jangan publish, bulk-edit, atau ubah permalink tanpa approval eksplisit di chat.
- Jangan gunakan FSE block theme penuh atau page builder berat (Elementor/Divi) sebagai basis tema.
- Jangan membuat file di luar `.workspaces/` tanpa alasan yang jelas (lihat bagian Workspace).
- Jangan operasikan situs WordPress mana pun selain yang tercantum di field URL `SITE.md` (lihat bagian WPVibe MCP).
- WordPress berada di server remote. Seluruh interaksi ke WordPress (manipulasi file tema, query data, manajemen konten) **wajib** dilakukan melalui WPVibe MCP, bukan melalui eksekusi command lokal.

## Definition of Done

Kategori & halaman statis terisi, draft tema disetujui, Lighthouse ≥80 (performa & SEO), tidak ada broken link, backup pra-publish terverifikasi.

## Changelog

Catat setiap pekerjaan yang selesai di repo ini. Entri terbaru di atas.

### `01. {{ YYYY-MM-DD }}`

- `{{ ringkasan singkat perubahan/pekerjaan yang selesai }}`
