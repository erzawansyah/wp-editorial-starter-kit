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
