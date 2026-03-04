#========================================
# Nama : Ghazyhibbban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#========================================

#========================================
# Latihan 2
#========================================

def insertion_sort(data):
 for i in range(1, len(data)):
    key = data[i]
    j = i - 1

 while j >= 0 and ________________:
    data[j + 1] = data[j]
    j -= 1

 ______________________

 return data

#Soal:
#1. Lengkapi kondisi agar menjadi sorting ascending.
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Kondisi Ascending
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

#2. Ubah agar menjadi descending.
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Kondisi Ascending
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data