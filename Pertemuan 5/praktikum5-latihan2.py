#=================================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#=================================================

#=================================================
# Latihan 2 : Tracing Rekursi
#=================================================

def countdown(n):

    # Base case (kondisi berhenti)
    # Jika n sudah 0, maka program mencetak "Selesai"
    # lalu fungsi berhenti (return)
    if n == 0:
        print("Selesai")
        return

    # Dicetak sebelum pemanggilan rekursi
    # Bagian ini dieksekusi saat fungsi "turun"
    print("Masuk:", n)

    # Recursive call (fungsi memanggil dirinya sendiri)
    # Nilai n dikurangi 1 setiap pemanggilan
    countdown(n - 1)

    # Dicetak setelah pemanggilan rekursi
    # Bagian ini dieksekusi saat fungsi "kembali" (naik)
    print("Keluar:", n)


# Memanggil fungsi
countdown(3)