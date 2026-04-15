#==============================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#==============================================
# Latihan 1 : Membuat Node
#==============================================

#Class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data= data  #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#membuat root
root = Node("A")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

#Penjelasan 
#Variabel data digunakan untuk menyimpan nilai utama, sementara left dan right berfungsi sebagai penunjuk (pointer) yang nantinya akan menghubungkan simpul tersebut ke anak-anaknya di bawah. 
# Melalui perintah root = Node("A"), kamu telah menciptakan titik pusat atau "akar" pohon, yang saat ini masih berdiri sendiri dengan nilai "A" dan belum memiliki cabang, sehingga ketika bagian kiri dan kanannya dipanggil, program akan menampilkan nilai kosong atau None.