#==============================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#==============================================
# Latihan 6 : Struktur Organisasi Perusahaan
#==============================================

#Fungsi preorder : root ==> Left ==> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#==============================================

#Class node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data= data  #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#Fungsi preorder : root ==> Left ==> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") #root
        preorder(node.left) #left
        preorder(node.right) #right


#Membuat Tree struktur organisasi
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

#Lanjutan child kanan level 2
root.right.right = Node("Staff3")


#Menjalankan Struktur Organisasi Perusahaan
print("Hasil Struktur Organisasi Perusahaan:")
preorder(root)