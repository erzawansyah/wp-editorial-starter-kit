# Title Psychology & Metadata Specifications

This guide establishes the rules for SERP `<title>`, on-page `H1`, and meta descriptions in Indonesian editorial publishing.

---

## 1. Title Distinction: SERP `<title>` vs On-Page `H1`

Never make `<title>` and `H1` identical. They serve different psychological and algorithmic goals:

### SERP `<title>` Tag (Search Engine Snippet)

- **Hard Limit:** Strictly under **60 characters** (approx. 580px desktop truncation limit).
- **Keyword Placement:** Place the exact primary keyword at or near the very start.
- **Brand Name Rule:** **Zero brand suffix**. Never append `| NamaBrand` or `- NamaBrand`. Every character belongs to high-intent terms and search value.

### On-Page `H1` (Visual Page Headline)

- **No Character Cap:** Can be 60–100 characters.
- **Editorial Grip:** Uses numbers, curiosity hooks, or direct value framing.
- **Keyword Requirement:** Must include the exact primary keyword or its natural variant.

---

## 2. Title Formulas by Article Type

| Content Type             | SERP `<title>` Formula (<60 chars)           | On-Page `H1` Formula                                                         |
| :----------------------- | :------------------------------------------- | :--------------------------------------------------------------------------- |
| **Comprehensive Pillar** | `Apa Itu [Topik]? Panduan Lengkap [Tahun]`   | `Mengenal [Topik]: Panduan Lengkap dan Cara Kerjanya di [Tahun]`             |
| **Numbered Listicle**    | `[Angka] Cara [Hasil Utama] untuk [Audiens]` | `#[Angka] Cara [Hasil Utama] yang Paling Efektif untuk [Audiens]`            |
| **Direct Comparison**    | `[X] vs [Y]: Perbedaan dan Mana yang Tepat`  | `Memilih Antara [X] atau [Y]: Analisis Perbedaan Kunci untuk Kebutuhan Anda` |
| **How-To Guide**         | `Cara [Aksi Inti]: Langkah Praktis [Tahun]`  | `Panduan Lengkap Cara [Aksi Inti] Langkah Demi Langkah untuk Pemula`         |

---

## 3. Meta Description Formula

- **Length:** Strictly **120 – 155 characters**. Complete sentence with a period.
- **Keyword:** Must contain the exact primary keyword.
- **Formula:**
  `[Direct Answer / Definition (~80 chars)] + [Click Value / Action Hook (~60 chars)].`
- **Example:**
  > _"Kredit Pemilikan Rumah subsidi menawarkan bunga tetap 5% bagi keluarga muda. Simak syarat lengkap dan langkah pengajuannya di sini."_ (138 characters).

---

## 4. End-of-Article Meta Output Block

Every generated article ends with a clean comment block:

```html
<!-- SEO Meta
meta_title: "Apa Itu Headless CMS? Panduan Arsitektur Web Modern"
meta_description: "Headless CMS memisahkan database konten dari antarmuka visual web. Pelajari cara kerja, keunggulan, dan contoh penerapannya di sini."
h1: "Mengenal Headless CMS: Arsitektur Pengelola Konten untuk Kebutuhan Web Modern"
primary_keyword: "Headless CMS"
secondary_keywords: "arsitektur web, cms modern, rest api wordpress"
target_length: ">1300 words"
style_applied: "Authoritative Industry Analysis"
-->
```
