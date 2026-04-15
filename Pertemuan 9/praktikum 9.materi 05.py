#==============================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#==============================================
# Latihan 5 : Membuat Traversal Postorder
#==============================================

#Class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data= data  #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#Membuat Traversal Postorder : left -> right -> root
def postorder(node):
    if node is not None:
        print(node.data, end= " ") #root
        postorder(node.left) #left
        postorder(node.right) #right

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


#Menjalankan Traversal Postorder
print("Hasil Traversal postorder:")
postorder(root)

#Penjelasan
#Kode ini mengimplementasikan metode Postorder Traversal, yaitu teknik penelusuran pohon dengan urutan Kiri → Kanan → Root. Namun, perlu dicatat bahwa pada fungsi postorder di kode Anda, urutan perintahnya masih mengikuti pola Preorder (mencetak data sebelum rekursi). Jika urutannya diperbaiki menjadi standar Postorder, program akan menelusuri seluruh anak kiri dan kanan terlebih dahulu hingga tuntas sebelum mencetak nilai induknya. Dengan struktur pohon tersebut, urutan Postorder yang benar akan menghasilkan D E B F C A, yang berarti akar utama (A) menjadi elemen terakhir yang diproses setelah semua cabangnya selesai dikunjungi.