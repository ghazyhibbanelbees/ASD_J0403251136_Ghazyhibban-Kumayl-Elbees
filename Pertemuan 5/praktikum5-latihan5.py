#=================================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#=================================================

#=================================================
# Latihan 5 : Generator PIN
#=================================================

def buat_pin(panjang, hasil=""):

    # Base case
    # Jika panjang PIN sudah sesuai,
    # maka cetak PIN dan berhenti
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Backtracking dengan perulangan angka 0–2
    # Setiap langkah akan mencoba semua kemungkinan angka
    for angka in ["0", "1", "2"]:

        # Recursive call
        # Tambahkan angka ke hasil sementara
        buat_pin(panjang, hasil + angka)


# Memanggil fungsi untuk membuat PIN 3 digit
buat_pin(3)

#Bagaimana cara mencegah angka yang sama muncul berulang?
#Saat ini program mengizinkan angka yang sama berulang, misalnya: 000, 111, 202
#Jika ingin mencegah angka yang sama muncul lebih dari sekali dalam satu PIN, kita perlu memastikan bahwa angka yang dipilih belum ada di hasil.

def buat_pin(panjang, hasil=""):

    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    for angka in ["0", "1", "2"]:

        # Cek agar angka tidak digunakan lebih dari sekali
        if angka not in hasil:
            buat_pin(panjang, hasil + angka)


buat_pin(3)

# Sekarang hanya muncul kombinasi tanpa angka yang sama, misalnya: 012,021,102
# Jumlahnya menjadi: 3! = 6
# Karena: Tidak boleh ada angka yang berulang
# Maka ini menjadi permutasi, bukan kombinasi biasa