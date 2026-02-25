#=================================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#=================================================

#=================================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
#input 3
# Masuk 3 - 2 - 1
# Keluar 1 - 2 - 3
#=================================================

def hitung(n):

    #base case
    if n == 0:
        print("selesai")
        return

    print("Masuk:", n)
    hitung(n-1) #recursive case
    print("keluar", n)

print("=======Program Tracing=========")
hitung(5)