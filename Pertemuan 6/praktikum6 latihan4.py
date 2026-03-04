#========================================
# Nama : Ghazyhibbban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#========================================

#========================================
# Latihan 4
#========================================

def merge_sort(data):
 if len(data) <= 1:
    return data

 mid = len(data) // 2
 left = data[:mid]
 right = data[mid:]

 left_sorted = merge_sort(left)
 right_sorted = merge_sort(right)

 return merge(left_sorted, right_sorted)


#Soal:
#1. Apa yang dimaksud dengan base case?
#Base case atau kondisi dasar adalah baris if len(data) <= 1: return data. Ini merupakan titik henti dari sebuah fungsi rekursif yang bertujuan untuk mencegah perulangan tanpa akhir (infinite loop). 
#Dalam Merge Sort, base case tercapai ketika sebuah list hanya memiliki satu elemen (atau kosong), karena secara logis list dengan satu elemen sudah dianggap terurut dan tidak perlu dibagi lagi.

#2. Mengapa fungsi memanggil dirinya sendiri?
#Fungsi memanggil dirinya sendiri (rekursi) pada baris merge_sort(left) dan merge_sort(right) untuk memecah masalah besar menjadi sub-masalah yang lebih kecil secara berulang. 
#Proses ini terus dilakukan hingga data benar-benar terpecah menjadi satuan terkecil (base case). Dengan cara ini, 
#algoritma dapat fokus menyelesaikan pengurutan pada bagian-bagian kecil terlebih dahulu sebelum nantinya digabungkan kembali secara teratur.

#3. Apa tujuan fungsi merge()?
#Tujuan utama fungsi merge() adalah untuk menyatukan kembali (combine) dua sub-list yang sudah terurut menjadi satu list baru yang tetap terurut. 
#Fungsi ini bekerja dengan membandingkan elemen-elemen terdepan dari kedua sub-list, mengambil yang terkecil, dan menyusunnya secara bertahap. 
#Tanpa fungsi merge(), data hanya akan terpecah-pecah tanpa pernah kembali menjadi satu kesatuan data yang utuh dan terurut.