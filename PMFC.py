import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmin yolunu belirtin
resim_yolu = "images/R.png"  # Örnek olarak

# Resmi yükleme
resim = cv2.imread(resim_yolu, cv2.IMREAD_GRAYSCALE)

# Resmin pixel değerlerini ekrana yazdırma
print("Pixel Değerleri: ")
print(resim)

# Resmin histogramını hesaplama
histogram = cv2.calcHist([resim], [0], None, [256], [0, 256])

# Histogramı çizdirme
plt.figure(figsize=(8, 6))
plt.plot(histogram, color='gray')
plt.title('Histogram')
plt.xlabel('Piksel Değeri')
plt.ylabel('Adet')
plt.show()


# import cv2
#
# # 10 resmin yollarını belirtin
# resim_yollari = ["images/image1.png", "images/image2.jpg", "images/image3.png", "images/image4.png", "images/image5.jpg",
#                  "images/image6.jpg", "images/image7.jpg", "images/image8.jpg", "images/image9.png", "images/image10.jpg"]
#
# # Her bir resmin pixel değerlerini ayrı dosyalara yazdırma
# for i, resim_yolu in enumerate(resim_yollari):
#     resim = cv2.imread(resim_yolu, cv2.IMREAD_GRAYSCALE)
#     dosya_adi = f"Pixel/resim_{i+1}_pixel_degerleri.txt"
#     with open(dosya_adi, "a") as dosya:
#         dosya.write("Pixel Değerleri:\n")
#         for deger in resim:
#             dosya.write(str(deger) + "\n")
#     print(f"{dosya_adi} dosyasına pixel değerleri yazıldı.")













# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 10 resmin yollarını belirtin
# resim_yollari = ["images/image1.png", "images/image2.jpg", "images/image3.png", "images/image4.png",
#                  "images/image5.jpg",
#                  "images/image6.jpg", "images/image7.jpg", "images/image8.jpg", "images/image9.png",
#                  "images/image10.jpg"]
#
# # Her bir resmin histogramını çizdirme
# for i, resim_yolu in enumerate(resim_yollari):
#     resim = cv2.imread(resim_yolu, cv2.IMREAD_GRAYSCALE)
#     histogram = cv2.calcHist([resim], [0], None, [256], [0, 256])
#
#     # Histogramı çizdirme
#     plt.figure(figsize=(8, 6))
#     plt.plot(histogram, color='gray')
#     plt.title(f'Histogram - Resim {i + 1}')
#     plt.xlabel('Piksel Değeri')
#     plt.ylabel('Adet')
#     plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
# # Toplam piksel değerlerini saklamak için bir liste oluşturun
# toplam_pixel_degerleri = []
#
# # Her bir dosyadan piksel değerlerini okuyun ve toplam listesine ekleyin
# for i in range(1, 11):  # 10 dosya var
#     dosya_adi = f"Pixel/resim_{i}_pixel_degerleri.txt"
#     with open(dosya_adi, "r") as dosya:
#         for satir in dosya:
#             if "Pixel Değerleri:" not in satir:
#                 pixel_degerleri = satir.strip().strip('[').strip(']').split()
#                 pixel_degerleri = list(map(int, pixel_degerleri))
#                 toplam_pixel_degerleri.extend(pixel_degerleri)
#
# # Toplam pixel değerlerini normalize etme
# toplam_pixel_degerleri = np.array(toplam_pixel_degerleri)
# toplam_pixel_degerleri = toplam_pixel_degerleri / 10  # 10 resim var, değerleri 8'e bölerek normalize ediyoruz
#
# # Toplam pixel değerlerinin histogramını hesaplayın
# histogram = np.histogram(toplam_pixel_degerleri, bins=256, range=(0, 256))[0]
#
# # Histogramı çizdirme
# plt.figure(figsize=(8, 6))
# plt.bar(np.arange(256), histogram, color='gray', width=1.0)
# plt.title('10 Resim pixel degerlerinin Histogramı Normalize Edilmiş Hali')
# plt.xlabel('Piksel Değeri')
# plt.ylabel('Adet')
# plt.show()


