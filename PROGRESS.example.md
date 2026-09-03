# PROGRESS.md - Tracker Progres Proyek

Salin file ini ke `.workspaces/PROGRESS.md` saat memulai proyek baru.
Update checklist ini secara **real-time** setiap kali satu item selesai dikerjakan.

---

**Proyek:** `{{ Nama Website }}`
**Dimulai:** `{{ YYYY-MM-DD }}`
**Target selesai:** `{{ YYYY-MM-DD }}`

---

## Setup (Manusia & Agen)

- [ ] Clone repo starter kit
- [ ] Buat direktori `.workspaces/assets/`
- [ ] Isi `SITE.md` dan `DESIGN.md` (atau jalankan `/wpsk-editorial-brainstorm`)
- [ ] Selesaikan semua item di `WORDPRESS-SETUP.md`
- [ ] WPVibe terkoneksi dan terverifikasi
- [ ] Tema GeneratePress diinstall dan aktif di server target
- [ ] Permalink diubah menjadi `/%postname%/` (hapus `index.php`)
- [ ] Salin file ini ke `.workspaces/PROGRESS.md`

---

## Fase Konten (@content)

### Kategori & Navigasi
- [ ] Daftar kategori final disetujui user
- [ ] Kategori dan Tag dibuat di WordPress (via WPVibe)
- [ ] Menu navigasi disusun

### Halaman Statis (via WPVibe)
- [ ] Tentang Kami
- [ ] Tim Redaksi
- [ ] Kebijakan Privasi
- [ ] Kontak
- [ ] `{{ Halaman statis lain sesuai niche }}`

### Aset
- [ ] Logo (format SVG + PNG) disimpan di `.workspaces/assets/`
- [ ] Favicon (format ICO + PNG 192px)
- [ ] OG image default (1200x630px)

### Konten Awal
- [ ] Minimal 3 draft artikel SEO per kategori utama diinjeksi via DB
- [ ] **HARD GATE:** Manusia melakukan *Visual Review* di tema GeneratePress dan menyatakan "Konten Siap".

---

## Fase Tema (@engineer)

### Build Tema
- [ ] Ganti nama `_tw` di `package.json` dan `file-header.css`
- [ ] Deklarasikan `add_theme_support('custom-logo')` di `functions.php`
- [ ] Template: `front-page.php` (homepage)
- [ ] Template: `header.php` (Elemen Navigasi Mutlak Dinamis)
- [ ] Template: `footer.php`
- [ ] Template: `single.php` (single post)
- [ ] Template: `page.php` (single page)
- [ ] Template: `archive.php` (kategori)
- [ ] Template: `search.php`
- [ ] Template: `404.php`
- [ ] Sidebar & Pagination diimplementasikan

### Handover
- [ ] Tema di-bundle (`npm run bundle`)
- [ ] File `.zip` dihasilkan dan terpisah dari *source folder*
- [ ] File `.workspaces/THEME_SPECS.md` digenerate sebagai dokumentasi teknis

---

## Fase QA (@qa)

- [ ] Lighthouse performa >= 80
- [ ] Lighthouse SEO >= 80
- [ ] Tidak ada broken link
- [ ] Responsif: tampilan mobile, tablet, desktop dicek
- [ ] Sitemap XML tersedia

---

## Deployment (Manusia)

- [ ] Backup pre-deploy tersimpan
- [ ] File tema `.zip` di-upload manual ke environment produksi
- [ ] Post-launch check: homepage, artikel, sitemap

---

## Catatan Proyek

`{{ Catat hambatan, keputusan desain, atau perubahan dari rencana awal di sini }}`

