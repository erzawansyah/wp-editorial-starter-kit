---
name: content-integrity
description: Standar integritas konten editorial Indonesia, zero halusinasi, hierarki sumber fakta 3-tier, diversitas author multi-etnis non-klise, format Gutenberg murni, dan featured image Pexafy.
trigger: always_on
---

# Content Integrity & Author Diversity Rules

Standar integritas konten, diversitas persona penulis, dan protokol penulisan artikel editorial di WordPress. Wajib dipatuhi oleh `@content` dan seluruh subagent penulisan.

---

## 1. Multi-Author & Diversitas Nama Indonesia

1. **Jumlah Author:**
   - Wajib membuat 3–5 akun user dengan peran `author` via REST API sebelum artikel mulai ditulis.
2. **Larangan Klise AI & Diversitas Nama:**
   - **DILARANG KERAS** menggunakan nama klise yang monoton dan repetitif (seperti nama yang berulang-ulang mengandung "Dimas" atau "Pramesti").
   - Wajib mengombinasikan latar belakang etnis realistis Indonesia: Jawa, Sunda, Minang, Batak, Melayu, Bugis/Makassar, Bali, Maluku/Papua.
3. **Format Email & Profil:**
   - Email format wajib: `<username>@<site.com>`.
   - Setiap author wajib memiliki bio realistis 2–3 kalimat yang mencerminkan otoritas niche situs.
4. **Larangan Mempublikasikan atas Nama Admin:**
   - **DILARANG KERAS** mempublikasikan artikel menggunakan akun `admin`.
   - Seluruh artikel yang diterbitkan wajib dirotasi secara merata di antara akun-akun author yang telah dibuat.

---

## 2. Standar Integritas & Anti-Slop Editorial

1. **Riset & Fakta Terverifikasi:**
   - Zero halusinasi data. Setiap artikel wajib mengutip 3–5 data konkret (regulasi, statistik resmi lembaga, tahun peluncuran).
   - Sumber Tier 1 (BPS, OJK, Bank Indonesia, Kemenkes, dokumentasi teknis resmi) dan Tier 2 (lembaga riset terkemuka, kantor berita resmi). Dilarang mengutip Tier 3 (blog anonim/farm content).
2. **Anti-Slop Copywriting & Formatting:**
   - Tanpa basa-basi pembuka klise (*"Di era digital saat ini..."*, *"Seperti yang kita tahu..."*). Langsung masuk ke jawaban/konteks inti (*Answer-First*).
   - Panjang paragraf terkontrol: 2–3 kalimat padat.
   - Hindari negasi kontras klise (*"Bukan hanya X, tapi juga Y"*), em-dash (—) berlebih, dan jargon AI (*delve, elevate, seamless, game-changer*).

---

## 3. Eksekusi Penulisan Paralel Subagents

1. **Paralel Multi-Subagent:**
   - Penulisan artikel wajib dilakukan secara paralel menggunakan subagents, bukan sekuensial satu per satu.
2. **Format Gutenberg Murni & Media Editorial:**
   - Konten wajib disusun menggunakan blok Gutenberg standar (paragraf, heading, list, quote, table) sesuai panduan `wp-patterns`.
   - Pencarian gambar/featured image wajib menggunakan **Pexafy MCP** (`search_photos`), diunduh dan diunggah ke Media Library WordPress via REST API, lalu disematkan sebagai featured image post.
