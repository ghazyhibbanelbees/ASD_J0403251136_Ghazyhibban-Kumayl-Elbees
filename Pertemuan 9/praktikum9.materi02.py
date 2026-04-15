#==============================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#==============================================
# Latihan 2 : Membuat Node
#==============================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data= data  #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#Membuat sebuah node root
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Lanjutan child kanan level 2
root.right.right = Node("F")
root.right.left = Node("G")

#menampilkan isi node
print("Data pada root", root.data)
print("Child kiri root", root.left)
print("Child kanan root", root.right)
print("Child kiri dari B:", root.left.left.data)
print("Child kanan dari B:", root.left.right.data)

print("Child kanan dari C:", root.right.right.data)
print("Child kiri dari C:", root.right.left.data)

#Lanjutkan kode programnya untuk keselurahan bagian tree -> tambahkan child di sisi kanan

#Penjelasan
#Mendefinisikan Root sebagai titik pusat dengan nilai "A", yang kemudian dicabangkan menjadi level satu melalui root.left (B) dan root.right (C). Struktur ini terus dikembangkan ke level dua dengan memberikan anak-anak pada simpul B dan C, sehingga menghasilkan formasi lengkap di mana simpul B memiliki anak D dan E, sementara simpul C memiliki anak G dan F.