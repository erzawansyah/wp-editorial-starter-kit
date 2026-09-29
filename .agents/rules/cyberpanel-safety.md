---
name: cyberpanel-safety
description: Protokol keselamatan mutlak interaksi server CyberPanel, OpenLiteSpeed, Cloudflare, MySQL, larangan mutasi server global, kewajiban konfirmasi deploy tema, dan peringatan wajib nonaktifkan API Access.
trigger: always_on
---

# CyberPanel & Server Operations Safety Rules

Aturan keselamatan mutlak dan protokol interaksi server (CyberPanel, OpenLiteSpeed, Cloudflare, MySQL, dan sistem berkas server).

---

## 1. Peringatan Keamanan & Hak Akses API

> [!CAUTION]
> **API ACCESS MEMBERIKAN KONTROL PENUH SERVER**
> Fitur API Access di CyberPanel memberikan izin tak terbatas mencakup pembuatan/penghapusan virtual host, modifikasi record DNS, manipulasi database MySQL, hingga akses bebas ke File Manager.

1. **Default Status API Access:**
   - Secara default, user dianjurkan menonaktifkan fitur API Access (*API Access = Disable*).
2. **Pengingat Wajib Setiap Selesai Task:**
   - Setiap kali agen selesai melakukan tugas provisi, deploy tema, atau operasi server, agen **WAJIB seketika itu juga mengingatkan pengguna**:
   > *"Seluruh operasi server telah selesai. Demi menjaga keamanan akun dan server, **pastikan fitur API ACCESS pada user CyberPanel segera dinonaktifkan** (Users > Modify User > API Access = Disable), karena API Access memberikan keleluasaan akses kontrol penuh."*

---

## 2. Konfirmasi Eksplisit Pengguna (Zero Unintended Mutations)

1. **Dilarang Modifikasi Global Tanpa Izin:**
   - Dilarang keras memodifikasi konfigurasi server global, vhost di luar domain target, listener OpenLiteSpeed global, atau database di luar scope project tanpa persetujuan eksplisit user.
2. **Konfirmasi Deploy Tema Otomatis:**
   - Sebelum mengunggah atau menimpa berkas tema di server live via skrip `cyberpanel_provisioner.py --deploy-theme`, agen **WAJIB bertanya dan meminta konfirmasi eksplisit pengguna**:
   > *"Bundle tema .zip telah siap. Apakah Anda ingin tema diunggah dan diekstrak langsung ke server CyberPanel (`wp-content/themes/`)?"*
   - Hanya jalankan eksekusi upload jika pengguna memberikan konfirmasi tegas.

---

## 3. Isolasi Multi-Akun & Kredensial

1. **Rotasi Kredensial `.env`:**
   - Baca kredensial CyberPanel dari variabel lingkungan `.env`:
     - `CYBERPANEL_URL`
     - `CYBERPANEL_USERNAME_1` / `CYBERPANEL_PASSWORD_1` (Domain primer)
     - `CYBERPANEL_USERNAME_2` / `CYBERPANEL_PASSWORD_2` (Domain sekunder/pembagian kuota)
     - Fallback: `CYBERPANEL_USERNAME` dan `CYBERPANEL_PASSWORD`
2. **Dilarang Hardcode:**
   - Dilarang keras menuliskan password, secret key, atau API token ke dalam kode sumber, commit git, file sementara, atau riwayat log.

---

## 4. Standar Wajib Konfigurasi Web Server & Easy MCP AI

Untuk menjamin kelancaran dan kestabilan komunikasi Model Context Protocol (MCP) antara AI client dan WordPress di lingkungan LiteSpeed/CyberPanel:

1. **Aturan `.htaccess` Authorization Header (Paling Atas):**
   - Agen/User **WAJIB** meletakkan blok rewrite authorization Easy MCP AI di **baris paling atas** file `.htaccess` (sebelum `# BEGIN LSCACHE` atau rewrite rules lainnya yang memiliki flag `[L]`):
     ```apache
     # BEGIN Easy MCP AI
     <IfModule mod_rewrite.c>
     RewriteEngine On
     RewriteCond %{HTTP:Authorization} .
     RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
     </IfModule>
     # END Easy MCP AI
     ```
   - *Tujuan:* Mencegah LiteSpeed/OpenLiteSpeed memotong (*strip*) header `Authorization: Bearer <token>` sebelum sampai ke runtime PHP/WordPress.

2. **Pengecualian Cache (LiteSpeed Cache Excludes):**
   - Wajib menambahkan endpoint berikut ke daftar **Do Not Cache URIs** (*LiteSpeed Cache > Cache > Excludes*):
     ```text
     /wp-json/easy-mcp-ai/
     /.well-known/oauth-
     /.well-known/openid-configuration
     ```
   - Opsi **Cache REST API** di LiteSpeed Cache **WAJIB DIMATIKAN (OFF / Disabled)** agar token, session, dan pemanggilan tool MCP tidak pernah tersimpan di cache server.
