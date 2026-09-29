# UPDATE.md — Panduan Pembaruan Template & Migrasi Proyek

Dokumen ini berisi panduan untuk menyinkronkan proyek website turunan (instance yang di-clone dari template lama) dengan pembaruan fitur, skrip, skill, dan standar konfigurasi terbaru dari template inti **WP Editorial Starter Kit**.

> [!NOTE]
> **Versi Template Saat Ini:** `2` (tersinkronisasi dengan `version.json`).
> Agen AI hanya akan membaca dokumen ini apabila terdeteksi perbedaan versi antara `version.json` dan file `.workspaces/PROGRESS.md` di proyek lokal Anda.

---

## 📌 Checklist Cepat Sebelum Melanjutkan Sesi Lama

Jika Anda kembali ke proyek yang pernah dibuat dari template ini dan agen mendeteksi perbedaan versi template:

1. [ ] **Periksa `.env` vs `.env.example`**: Bandingkan key yang ada di `.env.example`. Tambahkan key baru yang relevan ke `.env` lokal Anda.
2. [ ] **Periksa `.agents/mcp_config.json`**: Pastikan endpoint MCP mengarah ke konfigurasi target aktif.
3. [ ] **Periksa Ketersediaan MCP Client**: Pastikan MCP yang dibutuhkan (`easy_ai_mcp`, `pexafy`, dll.) aktif di Antigravity / client AI Anda.
4. [ ] **Perbarui Nomor Versi**: Setelah migrasi selesai, selaraskan nilai `**Template Version:**` di `.workspaces/PROGRESS.md` agar agen tidak membaca ulang dokumen ini.

---

## 🔄 Log Pembaruan per Versi

### [Version 2] — 2026-09-29: CyberPanel, Dynamic Frontpage, Anti-Slop Copy, Brand Assets & Rich Static Pages

Pembaruan besar yang memperluas otomatisasi infrastruktur, keamanan server, fleksibilitas kustomisasi tema, dan eliminasi bahasa AI sok keren pada antarmuka tema.

#### Apa yang Baru?
1. **Skill Provisi & Manajemen Server:**
   - **`wpsk-cyberpanel`** di `.agents/skills/wpsk-cyberpanel/`: Utilitas otomatisasi provisi Virtual Host, database MySQL, isolasi user, pengunggahan core WordPress, penulisan `wp-config.php` dengan salts resmi, dan sinkronisasi SSL listener.
   - **CLI Tool:** `.agents/skills/wpsk-cyberpanel/scripts/cyberpanel_provisioner.py` yang kini mendukung provisi penuh CMS dan opsi `--deploy-theme` untuk deploy tema otomatis.
2. **Skill Anti-Slop Copywriting:**
   - **`antislop-copywriting`** di `.agents/skills/antislop-copywriting/` (dari upstream `miqdadbadjuber/anti-slop`): Memfilter teks statis, CTA, microcopy, placeholder form, dan header agar bebas dari istilah klise AI (*unlock, elevate, delve, seamless, revolutionary, game-changer*, dsb.).
3. **Variabel Lingkungan Baru di `.env.example`:**
   - `CYBERPANEL_URL`
   - `CYBERPANEL_USERNAME`
   - `CYBERPANEL_PASSWORD`
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ZONE_ID`
4. **Aturan Baru Desain & Frontpage:**
   - **Frontpage Dinamis:** Dilarang meng-hardcode slug/ID kategori. Tema wajib menyediakan pengaturan (Customizer / Options) untuk pemilihan kategori, judul seksi, dan deskripsi, lengkap dengan fallback otomatis (`get_categories()`).
   - **Template Singular Page Anti-Polos (`page.php`):** Template singular page untuk post type `page` dilarang keras dibuat sekadar kotak putih polos; wajib memiliki hero page header elegan, wadah media sinematik, breadcrumb, dan tipografi Gutenberg luas.
5. **Workflow Aset Brand Sekuensial:**
   - Rangkaian 5 prompt brand berantai (*follow-up*) untuk ChatGPT/DALL-E 3 (Logo 16:5 tanpa tagline, Logo Inverse, Favicon 1:1, Favicon Rounded ber-backdrop, dan OG Image). Setiap prompt wajib berupa satu paragraf mengalir tunggal yang digenerate secara instruksional tanpa template engine kaku.
6. **Arsitektur Antigravity Harness (Modular Rules & Lifecycle Hooks):**
   - **Modular Rules (`.agents/rules/`):** Pemisahan guardrails ke file modular (`theme-guardrails.md`, `cyberpanel-safety.md`, `content-integrity.md`) untuk menjaga efisiensi context window serta memastikan ukuran file `AGENTS.md` tetap jauh di bawah batas 24KB harness.
   - **Lifecycle Hooks (`.agents/hooks.json` & `.agents/hooks/`):** Konfigurasi event hook `PreToolUse` pada `run_command` untuk validasi dan pengingat keselamatan saat mengeksekusi operasi server CyberPanel.

#### Instruksi untuk Pengguna Template Lama (v1 -> v2):
1. **Buka file `.env` proyek Anda**, dan tambahkan variabel berikut jika server hosting Anda menggunakan CyberPanel atau Cloudflare:
   ```env
   # ------------------------------------------------------------------------------
   # 3. CyberPanel (OpenLiteSpeed) Server & API Credentials (Skill: wpsk-cyberpanel)
   # ------------------------------------------------------------------------------
   CYBERPANEL_URL=https://your-server-ip-or-domain:8090/
   CYBERPANEL_USERNAME=your_cyberpanel_username
   CYBERPANEL_PASSWORD=your_cyberpanel_password

   # ------------------------------------------------------------------------------
   # 4. Cloudflare DNS & Proxy API (Opsional)
   # ------------------------------------------------------------------------------
   CLOUDFLARE_API_TOKEN=your_cloudflare_api_token
   CLOUDFLARE_ZONE_ID=your_cloudflare_zone_id
   ```
2. **Jika membuat site baru dari nol di CyberPanel:** Anda sekarang bisa meminta agen menjalankan provisi otomatis:
   ```powershell
   python .agents/skills/wpsk-cyberpanel/scripts/cyberpanel_provisioner.py `
     --domain example.com `
     --title "Judul Website" `
     --admin-user admin_user `
     --admin-email admin@example.com `
     --php "PHP 8.3"
   ```
3. **Deploy Tema Otomatis:** Anda kini dapat mengunggah paket ZIP tema langsung ke server via CyberPanel (memerlukan persetujuan eksplisit):
   ```powershell
   python .agents/skills/wpsk-cyberpanel/scripts/cyberpanel_provisioner.py --domain example.com --deploy-theme .workspaces/nama-tema.zip
   ```
4. **Peringatan Keamanan Wajib:** Setelah operasi CyberPanel selesai, **selalu nonaktifkan kembali fitur API Access** pada user CyberPanel terkait (*Users > Modify User > API Access = Disable*).
5. **Konfigurasi Frontpage Dinamis:** Pastikan `front-page.php` tidak lagi meng-hardcode slug kategori, melainkan menggunakan pengaturan kustom (Customizer / Options) dengan fallback dinamis otomatis (`get_categories()`).
6. **Desain Template Singular Page Anti-Polos:** Pastikan template `page.php` mengadopsi hero header elegan, breadcrumbs, dan styling Tailwind Typography Gutenberg.
7. **Filter Anti-Slop Copywriting:** Tinjau teks statis UI dan tombol CTA menggunakan aturan di `antislop-copywriting` agar bebas jargon klise AI.
8. **Update `.workspaces/PROGRESS.md`**: Ubah `**Template Version:** 1` menjadi `**Template Version:** 2`.

---

### [Version 1] — 2026-09-14: Pondasi Awal, Easy MCP AI & Pexafy

Versi awal template dengan arsitektur Content-First, integrasi Easy MCP AI, dan Pexafy MCP.

#### Ringkasan:
- Integrasi **Easy MCP AI** untuk interaksi remote WordPress via MCP endpoint (`.agents/mcp_config.json`).
- Integrasi **Pexafy MCP** untuk pencarian foto editorial otomatis.
- Arsitektur **Content-First**: Pembuatan author beragam (anti-Dimas/Pramesti), taksonomi, halaman statis, dan menu sebelum koding tema.
- Standar visual **`wpsk-theme-craft`** (Impeccable commands, 8 aturan baku, full-page screenshot Playwright 1440px & 375px).

---

## 💡 Mekanisme AI Token Optimization

1. Di setiap awal sesi, agen hanya membaca angka `template_version` dari `version.json` dan membandingkannya dengan baris `**Template Version:**` di `.workspaces/PROGRESS.md`.
2. **Jika versi sama**, agen **TIDAK AKAN membaca `UPDATE.md`** sehingga menghemat context window dan token secara signifikan.
3. **Hanya jika versi berbeda (atau belum ada)**, agen membuka section versi terkait di dokumen ini untuk memberikan notifikasi proaktif kepada pengguna.
