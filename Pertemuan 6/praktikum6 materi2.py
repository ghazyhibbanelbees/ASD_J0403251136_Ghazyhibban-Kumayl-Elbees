#========================================
# Nama : Ghazyhibbban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#========================================

#========================================
# Insertion Sort dengan tracing
#========================================

def insertion_sort(data):
        
         #melihat data awal
        print("Data Awal: ", data)
        print("="*50)

        #Loop mulai dari data ke 2 (index array ke 1)
        for i in range(1, len(data)):

            key = data[i] #Simpan nilai yang disisipkan
            j = i-1 #index elemen terakhir di bagian kiri

            print("Iterasi ke 1- ", i)
            print("Nilai key = ", key)
            print("Bagian kiri (terurut): ", data[i:])
            print("Bagian Kanan (belum terurut): ", data[i:])

            #Geser
            while j>=0 and data[j] > key:
                data[j+1] = data[j]
                j -= 1
            #sisipkan key ke posisi yang benar
            data[j+1] = key

            print("Setelah disisipkan: ", data)
            print("-"*50)
        return data

angka = [1,12,17,23,5,6]
print("Hasil Sorting: ", insertion_sort(angka))