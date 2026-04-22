#=========================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM: J0403251136
# Kelas : B1
#=========================================

#=========================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
#=========================================

class Node:
    """Class untuk menciptakan objek Node/titik pohon."""
    def __init__(self, data):
        self.data = data    # Menyimpan nilai angka
        self.left = None    # Penunjuk ke anak kiri (nilai < root)
        self.right = None   # Penunjuk ke anak kanan (nilai > root)

# FUNGSI UTAMA: ROTASI KIRI 
def rotate_left(x):
    """Fungsi untuk menggeser node agar pohon lebih seimbang."""
    
    # 1. Tentukan y sebagai anak kanan dari x (calon root baru)
    y = x.right 
    
    # 2. T2 adalah subtree kiri milik y (jika ada). 
    # Kita simpan sementara agar tidak hilang saat posisi y berubah.
    T2 = y.left 

    # --- PROSES ROTASI ---
    
    # 3. Pindahkan x menjadi anak kiri dari y.
    # Secara logika, y naik ke atas, dan x turun menjadi anak kirinya.
    y.left = x 
    
    # 4. Ambil T2 yang disimpan tadi, pasang sebagai anak kanan x.
    # Karena posisi kanan x sebelumnya diisi y, sekarang digantikan oleh T2.
    x.right = T2 

    # 5. Kembalikan y karena sekarang dia adalah root yang baru.
    return y

# FUNGSI PEMBANTU 
def preorder(root):
    """Menampilkan urutan: Root -> Kiri -> Kanan."""
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def tampil_struktur(root, level=0, posisi="Root"):
    """Menampilkan visualisasi pohon secara bertingkat."""
    if root is not None:
        # Memberikan spasi sesuai level agar terlihat hierarkinya
        print("  " * level + f"|-- {posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# =========================================
# PROGRAM UTAMA
# =========================================

# Membuat pohon manual yang miring ke kanan (10 -> 20 -> 30)
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("--- Sebelum Rotasi Kiri ---")
print("Preorder:", end=" ")
preorder(root)
print