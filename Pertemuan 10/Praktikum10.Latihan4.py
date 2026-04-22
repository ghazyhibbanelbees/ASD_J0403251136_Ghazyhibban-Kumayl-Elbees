#=========================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM: J0403251136
# Kelas : B1
#=========================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
#=========================================

class Node:
    """Class untuk merepresentasikan node dalam pohon."""
    def __init__(self, data):
        self.data = data   # Menyimpan nilai angka
        self.left = None   # Penunjuk ke anak kiri (nilai < root)
        self.right = None  # Penunjuk ke anak kanan (nilai > root)

# FUNGSI UTAMA: ROTASI KANAN 
def rotate_right(y):
    """
    Fungsi untuk melakukan rotasi kanan.
    y adalah root lama yang akan diturunkan ke kanan.
    """
    # 1. Tentukan x sebagai anak kiri dari y (calon root baru)
    x = y.left 
    
    # 2. Amankan subtree kanan milik x ke variabel sementara T2.
    # Ini dilakukan agar data tersebut tidak hilang saat posisi x bergeser.
    T2 = x.right 

    # PROSES ROTASI 
    
    # 3. y dijadikan sebagai anak kanan dari x.
    # Secara visual, x naik ke atas dan y ditarik turun ke sisi kanan x.
    x.right = y 
    
    # 4. Pasang kembali T2 sebagai anak kiri dari y.
    # Karena anak kiri y (yaitu x) sudah naik, maka kekosongannya diisi oleh T2.
    y.left = T2 

    # 5. Kembalikan x sebagai root baru bagi struktur pohon ini.
    return x

# FUNGSI PENDUKUNG 
def preorder(root):
    """Menampilkan data dengan urutan Root -> Kiri -> Kanan."""
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def tampil_struktur(root, level=0, posisi="Root"):
    """Menampilkan visualisasi struktur hierarki pohon."""
    if root is not None:
        print("  " * level + f"|-- {posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# =========================================
# PROGRAM UTAMA
# =========================================

# 1. Membuat pohon yang miring ke kiri (30 -> 20 -> 10)
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("--- Kondisi SEBELUM Rotasi Kanan ---")
print("Preorder:", end=" ")
preorder(root)
print("\nStruktur:")
tampil_struktur(root)

# 2. Melakukan rotasi kanan pada root (node 30)
root = rotate_right(root)

print("\n" + "="*35)
print("--- Kondisi SESUDAH Rotasi Kanan ---")
print("Preorder:", end=" ")
preorder(root)
print("\nStruktur:")
tampil_struktur(root)