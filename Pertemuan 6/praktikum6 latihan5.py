#========================================
# Nama : Ghazyhibbban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#========================================

#========================================
# Latihan 5
#========================================

def merge(left, right):
   result = []
   i = 0
   j = 0

   while i < len(left) and j < len(right):
     if left[i] <= right[j] :
        result.append(left[i])
        i += 1
     else:
        result.append(right[j])
        j += 1
      
        result.extend(left[i:])
        result.extend(right[j:])
      
        return result


#Soal:
#1. Lengkapi kondisi agar menjadi ascending.
#left[i] <= right[j]


#2. Jelaskan fungsi result.extend().
#Fungsi result.extend() digunakan untuk menyalin semua elemen yang tersisa dari salah satu sub-list (left atau right) ke dalam list hasil akhir. 
#Dalam proses looping while, biasanya akan ada satu list yang habis lebih dulu sementara list lainnya masih memiliki sisa angka yang sudah terurut. 
#Karena angka-angka sisa tersebut dipastikan lebih besar dari semua angka yang sudah masuk ke result, kita cukup "menempelkan" semuanya sekaligus di bagian akhir tanpa perlu dibandingkan lagi satu per satu.
