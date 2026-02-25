#=================================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#=================================================

#=================================================
# Latihan 3 : Mencari Nilai
#=================================================

def cari_maks(data, index=0):

    # Base case (kondisi berhenti)
    # Jika index sudah berada di elemen terakhir list,
    # maka langsung kembalikan nilai elemen tersebut
    if index == len(data) - 1:
        return data[index]

    # Recursive call
    # Fungsi memanggil dirinya sendiri untuk mengecek
    # elemen berikutnya (index + 1)
    maks_sisa = cari_maks(data, index + 1)

    # Membandingkan elemen saat ini dengan hasil maksimum sisa elemen
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]

# Memanggil fungsi untuk mencari nilai maksimum
print("Nilai maksimum:", cari_maks(angka))