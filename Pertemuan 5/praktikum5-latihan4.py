#=================================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#=================================================

#=================================================
# Latihan 4 : Kombinasi Huruf
#=================================================

def kombinasi(n, hasil=""):

    # Base case
    # Jika panjang string sudah sama dengan n,
    # maka cetak hasil kombinasi dan berhenti
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive call 1
    # Tambahkan huruf "A" ke hasil
    kombinasi(n, hasil + "A")

    # Recursive call 2
    # Tambahkan huruf "B" ke hasil
    kombinasi(n, hasil + "B")


# Memanggil fungsi
kombinasi(2)

#Bagaimana Jumlah Kombinasi Dihasilkan?
#Setiap posisi memiliki 2 kemungkinan:
#A
#B
#Jika panjang kombinasi adalah n, maka jumlah total kombinasi: 2n
#Karena:Setiap karakter memiliki 2 pilihan dan ada n posisi