# PROGRESS.md — Tracker Progres Proyek

Salin file ini ke `.workspaces/PROGRESS.md` saat memulai proyek baru.
Update checklist ini setiap kali satu item selesai dikerjakan.

---

**Proyek:** `{{ Nama Website }}`
**Dimulai:** `{{ YYYY-MM-DD }}`
**Target selesai:** `{{ YYYY-MM-DD }}`

---

## Setup (Manusia)

- [ ] Clone repo starter kit
- [ ] Isi `SITE.md` (semua field Identitas)
- [ ] Isi `DESIGN.md` (front matter YAML + semua seksi)
- [ ] Install WordPress di server
- [ ] Selesaikan semua item di `WORDPRESS-SETUP.md`
- [ ] WPVibe terkoneksi dan terverifikasi
- [ ] Salin file ini ke `.workspaces/PROGRESS.md`

---

## Fase Konten (@content)

### Kategori
- [ ] Daftar kategori final disetujui user
- [ ] Kategori dibuat di WordPress (dengan slug, deskripsi)
- [ ] Menu header tersusun dari kategori tersebut

### Halaman Statis
- [ ] Tentang Kami
- [ ] Tim Redaksi
- [ ] Kebijakan Privasi
- [ ] Kontak
- [ ] `{{ Halaman statis lain sesuai niche }}`

### Aset
- [ ] Logo (format SVG + PNG)
- [ ] Favicon (format ICO + PNG 192px)
- [ ] OG image default (1200×630px)

### Konten Awal
- [ ] Minimal 3 draft artikel per kategori utama
- [ ] Semua draft sudah di-review dan disetujui sebelum publish

---

## Fase Tema (@architect → @engineer)

### Wireframe (@architect)
- [ ] Wireframe homepage disetujui
- [ ] Wireframe single post disetujui
- [ ] Wireframe archive/kategori disetujui

### Build Tema (@engineer)
- [ ] Struktur folder tema dibuat
- [ ] `style.css` + `functions.php` dasar
- [ ] Tailwind CSS terkonfigurasi
- [ ] Template: `index.php` (homepage)
- [ ] Template: `header.php`
- [ ] Template: `footer.php`
- [ ] Template: `single.php` (single post)
- [ ] Template: `page.php` (single page)
- [ ] Template: `archive.php` (kategori)
- [ ] Template: `search.php`
- [ ] Template: `404.php`
- [ ] Sidebar (jika diaktifkan)
- [ ] Tema diaktifkan di situs (dari draft ke aktif setelah disetujui)

---

## Fase QA (@qa)

- [ ] Lighthouse performa ≥ 80
- [ ] Lighthouse SEO ≥ 80
- [ ] Tidak ada broken link
- [ ] Responsif: tampilan mobile, tablet, desktop dicek
- [ ] Form kontak berfungsi
- [ ] Sitemap XML tersedia
- [ ] Robots.txt benar (tidak memblokir crawler)
- [ ] OG tags terpasang di semua template

---

## Deployment (Manusia)

- [ ] Backup pre-deploy tersimpan (via UpdraftPlus atau manual)
- [ ] Review final oleh Leader/PIC
- [ ] Approval deploy diberikan
- [ ] Dipromosikan ke environment produksi
- [ ] DNS/domain diarahkan ke server produksi
- [ ] SSL aktif dan berfungsi (HTTPS)
- [ ] Post-launch check: homepage, artikel, form, sitemap

---

## Catatan Proyek

`{{ Catat hambatan, keputusan desain, atau perubahan dari rencana awal di sini }}`
