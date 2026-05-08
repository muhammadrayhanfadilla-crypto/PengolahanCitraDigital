# Pengolahan Citra Digital

# Implementasi Deteksi Tepi Citra Menggunakan Metode Canny Edge Detection

---

## Tentang Project

Project ini dibuat sebagai bagian dari tugas UTS mata kuliah Pengolahan Citra Digital.

Fokus utama dari project ini adalah mengimplementasikan teknik deteksi tepi pada citra digital menggunakan metode **Canny Edge Detection** untuk menemukan batas objek pada gambar dan meningkatkan analisis visual citra.

---

# Tujuan

* Memahami konsep dasar deteksi tepi pada citra digital
* Mengimplementasikan metode deteksi tepi menggunakan algoritma Canny
* Mengamati perubahan citra sebelum dan sesudah proses deteksi tepi
* Menganalisis hasil pendeteksian objek pada gambar

---

# Landasan Teori

## 1. Citra Digital

Citra digital merupakan representasi visual dalam bentuk data numerik yang dapat diproses menggunakan komputer.

Citra digital terdiri dari kumpulan piksel yang menyimpan informasi warna maupun intensitas.

---

## 2. Deteksi Tepi pada Citra

Deteksi tepi adalah proses untuk menemukan batas atau perubahan intensitas yang signifikan pada suatu gambar.

Deteksi tepi sering digunakan dalam:

* Pengenalan objek
* Segmentasi citra
* Computer Vision
* Analisis bentuk objek

---

## 3. Metode Deteksi Tepi

### 🔹 Canny Edge Detection

Metode Canny merupakan salah satu algoritma deteksi tepi yang paling populer dalam pengolahan citra digital.

Algoritma ini bekerja melalui beberapa tahapan:

1. Noise reduction menggunakan Gaussian Blur
2. Menghitung gradien intensitas
3. Non-maximum suppression
4. Double threshold
5. Edge tracking by hysteresis

### Kelebihan:

* Hasil deteksi tepi lebih jelas
* Mampu mengurangi noise
* Akurasi cukup baik

### Kekurangan:

* Membutuhkan parameter threshold yang tepat
* Proses lebih kompleks dibanding metode sederhana

---

# Implementasi

## Tools yang Digunakan

* Python
* OpenCV
* NumPy
* Matplotlib

---

# Instalasi Library

```bash
pip install opencv-python numpy matplotlib
```

---

# Struktur Folder

```text
PengolahanCitraDigital/
│
├── assets/
│   └── gambar.jpg
│
├── output/
│
└── main.py
```

---

# Alur Proses

1. Membaca citra dari folder assets
2. Mengubah citra menjadi grayscale
3. Melakukan Gaussian Blur untuk mengurangi noise
4. Menerapkan metode Canny Edge Detection
5. Menampilkan dan menyimpan hasil

---

# Cara Menjalankan Program

```bash
python main.py
```

---

# Hasil Output

Program akan menghasilkan:

* Grayscale Image
* Gaussian Blur Image
* Canny Edge Detection Image

Semua hasil akan otomatis tersimpan pada folder:

```text
output/
```

---

# Analisis

* Metode Canny berhasil mendeteksi tepi objek pada citra
* Gaussian Blur membantu mengurangi noise sebelum proses deteksi
* Tepi objek terlihat lebih jelas dibanding gambar asli
* Hasil deteksi dipengaruhi oleh nilai threshold yang digunakan
* Metode ini cocok digunakan dalam analisis objek dan computer vision

---

# Kesimpulan

Deteksi tepi citra digital dapat dilakukan menggunakan metode Canny Edge Detection.

Kesimpulan dari project ini:

* Metode Canny efektif untuk mendeteksi tepi objek
* Hasil deteksi cukup jelas dan detail
* Gaussian Blur membantu meningkatkan kualitas deteksi
* Metode ini cocok untuk dasar analisis citra digital

---

# Penutup

Terima kasih telah melihat project ini.

Semoga project ini dapat memberikan manfaat dan menjadi langkah awal dalam memahami proses deteksi tepi dalam pengolahan citra digital.
