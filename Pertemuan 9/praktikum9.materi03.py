#==============================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#==============================================
# Latihan 3 : Membuat Traversal Preorder
#==============================================

#Class node digunakan untuk dasar pada tree

class Node:
    def __init__(self, data):
        self.data= data  #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#Fungsi preorder : root ==> Left ==> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


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


#Menjalankan Traversal Preorder
print("Hasil Traversal Preorder:")
preorder(root)

#Penjelasan
#Kode ini menerapkan metode Preorder Traversal, yaitu teknik membaca pohon dengan urutan Root → Kiri → Kanan. Melalui fungsi rekursif preorder, program akan mencetak nilai simpul saat ini terlebih dahulu, kemudian menelusuri seluruh cabang kiri hingga tuntas, baru terakhir menyisir cabang kanan. Dengan struktur pohon yang Anda buat, hasil urutan pembacaannya adalah A B D E C F, yang menunjukkan bagaimana data diakses secara sistematis dari akar menuju daun terdalam di sisi kiri sebelum berpindah ke sisi kanan