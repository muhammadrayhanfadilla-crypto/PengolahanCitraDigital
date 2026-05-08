import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# PROJECT UTS PENGOLAHAN CITRA DIGITAL
# IMPLEMENTASI DETEKSI TEPI MENGGUNAKAN
# METODE CANNY EDGE DETECTION


# Membuat folder output jika belum ada
if not os.path.exists("output"):
    os.makedirs("output")


# Lokasi gambar
image_path = "assets/gambar.jpg"

# Membaca gambar
image = cv2.imread(image_path)

# Mengecek apakah gambar berhasil dibaca
if image is None:
    print("ERROR: Gambar tidak ditemukan!")
    print("Pastikan file gambar ada di folder assets")
    exit()

# Mengubah warna BGR ke RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# KONVERSI KE GRAYSCALE


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# GAUSSIAN BLUR
# Mengurangi noise pada gambar


blur = cv2.GaussianBlur(gray, (5, 5), 0)


# CANNY EDGE DETECTION


edges = cv2.Canny(blur, 100, 200)


# MENYIMPAN HASIL

cv2.imwrite("output/grayscale.jpg", gray)
cv2.imwrite("output/blur.jpg", blur)
cv2.imwrite("output/canny_edges.jpg", edges)


# MENAMPILKAN HASIL


plt.figure(figsize=(15, 10))

# Gambar Original
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

# Grayscale
plt.subplot(2, 2, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

# Gaussian Blur
plt.subplot(2, 2, 3)
plt.imshow(blur, cmap="gray")
plt.title("Gaussian Blur")
plt.axis("off")

# Canny Edge Detection
plt.subplot(2, 2, 4)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()


# INFORMASI


print("======================================")
print("PROSES DETEKSI TEPI SELESAI")
print("======================================")
print("Hasil disimpan di folder output/")
print("- grayscale.jpg")
print("- blur.jpg")
print("- canny_edges.jpg")
print("======================================")