#=================================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#=================================================

#=================================================
# Latihan 1 : Rekursi Pangkat
#=================================================

def pangkat(a, n):
  # Base case (kondisi berhenti)
  # Jika pangkat sudah 0, maka hasilnya adalah 1
  # karena secara matematika a^0 = 1
 if n == 0:
    return 1
 
 # Recursive case (pemanggilan fungsi ke dirinya sendiri)
 # Fungsi akan mengalikan a dengan hasil pangkat(a, n-1)
 # Nilai n akan terus berkurang sampai mencapai 0
 return a * pangkat(a, n - 1)


# Memanggil fungsi
# Artinya menghitung 2^4 
print(pangkat(2, 4))