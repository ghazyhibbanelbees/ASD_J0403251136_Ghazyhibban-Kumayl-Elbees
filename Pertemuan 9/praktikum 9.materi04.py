#==============================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#==============================================
# Latihan 4 : Membuat Traversal Inorder
#==============================================

#Class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data= data  #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#Membuat fungsi Inorder : left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end= " ")
        inorder(node.right)



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


#Menjalankan Traversal Inorder
print("Hasil Traversal inorder:")
inorder(root)

#Penjelasan
#Kode ini menerapkan metode Inorder Traversal, yaitu teknik pembacaan pohon dengan urutan Kiri → Root → Kanan. Melalui fungsi rekursif inorder, program akan terus menelusuri cabang kiri hingga mencapai titik terdalam sebelum mencetak data simpul tersebut, baru kemudian memproses akar dan beralih ke cabang kanan. Berdasarkan struktur yang Anda buat, proses ini menghasilkan urutan D B E A C F, yang secara logis membentangkan elemen pohon dari sisi paling kiri hingga ke sisi paling kanan.