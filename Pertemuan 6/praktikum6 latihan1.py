#========================================
# Nama : Ghazyhibbban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#========================================

#========================================
# Latihan 1
#========================================

def insertion_sort(data):
 for i in range(1, len(data)):
    key = data[i]
    j = i - 1

 while j >= 0 and data[j] > key:
   data[j + 1] = data[j]
   j -= 1
   
   data[j + 1] = key

 return data

#Soal:
#1. Mengapa perulangan dimulai dari indeks 1?
#Perulangan dimulai dari indeks 1 (range(1, len(data))) karena algoritma ini menganggap elemen pertama (indeks 0) sebagai bagian yang sudah terurut. 
#Tidak ada gunanya membandingkan elemen pertama dengan dirinya sendiri. Jadi, kita mulai dari elemen kedua (indeks 1) untuk dibandingkan dengan elemen-elemen di sebelah kirinya.

#2. Apa fungsi variabel key?
#Variabel key berfungsi sebagai penampung sementara untuk nilai yang sedang ingin kita pindahkan

#3. Mengapa digunakan while, bukan for?
#Penggunaan loop while jauh lebih tepat dibandingkan for dalam konteks ini karena jumlah iterasi ke arah kiri bersifat tidak pasti atau kondisional. Loop while memungkinkan algoritma untuk berhenti seketika (early exit) saat ia menemukan elemen yang nilainya sudah lebih kecil dari key atau saat sudah mencapai batas awal indeks (0). 
#Jika menggunakan for, program akan dipaksa memeriksa seluruh elemen di sebelah kiri secara kaku, padahal posisi yang tepat mungkin sudah ditemukan di tengah jalan, sehingga penggunaan while membuat algoritma menjadi lebih efisien secara komputasi.

#4. Operasi apa yang terjadi di dalam while?
#Operasi utama yang terjadi di dalam blok while adalah pergeseran elemen (shifting) secara bertahap ke arah kanan untuk menciptakan ruang bagi elemen key. Pada baris data[j + 1] = data[j], nilai yang lebih besar dari key disalin ke posisi indeks di depannya, sehingga seolah-olah elemen tersebut bergerak mundur satu langkah. 
#Proses ini dilakukan berulang kali selama kondisi terpenuhi, hingga akhirnya ditemukan posisi yang kosong dan tepat di mana key tidak lagi lebih kecil dari elemen di sebelah kirinya, barulah proses pergeseran berhenti.