#=========================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM: J0403251136
# Kelas : B1
#=========================================

class Node:
    """Class Node: Cetakan untuk setiap titik di dalam pohon."""
    def __init__(self, data):
        self.data = data # Menyimpan nilai angka
        self.left = None # Penunjuk ke anak kiri (nilai < root)
        self.right = None # Penunjuk ke anak kanan (nilai > root)

def insert(root, data):
    """Fungsi Insert: Menempatkan data baru di posisi yang tepat."""
    # Jika tempat masih kosong, buat node baru di sini
    if root is None:
        return Node(data)
    
    # ALUR LOGIKA:
    # 1. Jika data baru < data sekarang, belok ke kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # 2. Jika data baru > data sekarang, belok ke kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    # Kembalikan struktur pohon yang sudah diperbarui
    return root

def preorder(root):
    """Traversal Preorder: Cetak dengan urutan Root -> Kiri -> Kanan."""
    if root is not None:
        print(root.data, end=" ") # Cetak data diri sendiri dulu
        preorder(root.left)       # Kemudian cek ke bawah kiri
        preorder(root.right)      # Terakhir cek ke bawah kanan

def tampil_struktur(root, level=0, posisi="Root"):
    """Fungsi Visualisasi: Menampilkan hierarki pohon secara vertikal."""
    if root is not None:
        # Gunakan spasi (indentasi) untuk menunjukkan kedalaman (level)
        print("  " * level + f"|-- {posisi}: {root.data}")
        # Rekursif ke kiri dan kanan dengan level yang bertambah
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# ----------------------------------------
# PROGRAM UTAMA
# ----------------------------------------

root = None
# Skenario: Data dimasukkan secara urut naik (10, 20, 30)
data_list = [10, 20, 30]

print("--- Memasukkan Data ---")
for data in data_list:
    root = insert(root, data)

print("\nPreorder BST:")
preorder(root)

print("\n\nStruktur BST (Visualisasi):")
tampil_struktur(root)