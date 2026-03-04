#========================================
# Nama : Ghazyhibbban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#========================================

#========================================
# Latihan 3
#========================================

def insertion_sort(data):
    print(f"Data awal: {data}")
    print("-" * 30)
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        # Proses pergeseran (shifting)
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        # Menempatkan key di posisi yang tepat
        data[j + 1] = key
        
        # Menampilkan hasil setiap iterasi
        print(f"Iterasi i={i} (key={key}): {data}")

    return data

angka = [5, 2, 4, 6, 1, 3]
hasil_akhir = insertion_sort(angka)

print("-" * 30)
print(f"Data akhir terurut: {hasil_akhir}")


#Soal:
#1. Tuliskan isi list setelah iterasi i = 1.
#Setelah Iterasi i = 1: [2, 5, 4, 6, 1, 3]

#2. Tuliskan isi list setelah iterasi i = 3.
#Setelah Iterasi i = 3: [2, 4, 5, 6, 1, 3]

#3. Berapa kali pergeseran terjadi pada iterasi i = 4?
#Total pergeseran pada i = 4 adalah 4 kali.
#(List menjadi [1, 2, 4, 5, 6, 3] setelah iterasi ini selesai).