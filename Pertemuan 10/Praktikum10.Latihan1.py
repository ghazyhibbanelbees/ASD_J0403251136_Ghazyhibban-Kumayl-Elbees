#=========================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM: J0403251136
# Kelas : B1
#=========================================

class Node:
    """Kelas untuk merepresentasikan satu titik (node) dalam pohon."""
    def __init__(self, data):
        self.data = data   # Menyimpan nilai angka
        self.left = None   # Penunjuk ke anak kiri (nilai < root)
        self.right = None  # Penunjuk ke anak kanan (nilai > root)
        
#=============================================================
# LATIHAN 1: FUNGSI INSERT 
#=============================================================


def insert(root, data):
    """Fungsi untuk menyisipkan data baru ke dalam BST."""
    # Jika pohon kosong, buat node baru sebagai root
    if root is None:
        return Node(data)
    
    # Alur Logika Insert:
    # 1. Jika data lebih kecil, bergerak ke cabang kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # 2. Jika data lebih besar, bergerak ke cabang kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    
    # Balikkan root yang telah dimodifikasi
    return root


#====================================================================
#LATIHAN 2: TRAVERSAL INORDER
#====================================================================


def inorder(root):
    """Fungsi untuk menampilkan semua data secara terurut (Kiri-Root-Kanan)."""
    if root is not None:
        inorder(root.left)           # Kunjungi semua di sebelah kiri
        print(root.data, end=" ")    # Cetak data root/tengah
        inorder(root.right)          # Kunjungi semua di sebelah kanan


#====================================================================
# LATIHAN 3: SEARCH DI BST 
#====================================================================

def search(root, key):
    """Fungsi untuk mencari nilai tertentu di dalam BST."""
    # Jika root kosong atau data ditemukan di root
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    # Alur Logika Search:
    # Jika kunci < data root, hanya cari di cabang kiri
    if key < root.data:
        return search(root.left, key)
    # Jika kunci > data root, hanya cari di cabang kanan
    else:
        return search(root.right, key)
    
#Program Utama
# 1. Membangun Pohon
root = None
data_list = [50, 30, 70, 20, 40, 50, 80]

print("--- Proses Pembuatan BST ---")
for data in data_list:
    root = insert(root, data)
print("BST berhasil dibuat.\n")

# 2. Menampilkan Data (Inorder)
print("--- Hasil Traversal Inorder (Data Terurut) ---")
inorder(root)
print("\n")

# 3. Menguji Pencarian
print("--- Uji Pencarian Data ---")
key = 40
if search(root, key):
    print(f"Data {key} ditemukan di dalam BST.")
else:
    print(f"Data {key} tidak ditemukan.")