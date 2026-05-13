# =========================================================
# Nama: Ghazyhibban Kumayl Elbees
# Nim: J0403251136
# Kelas: B1
# ==========================================================
# Materi 1: Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
# Representasi graph dalam bentuk list of tuples agar mudah diurutkan
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil secara menaik (Ascending)
# Ini adalah langkah utama dalam Algoritma Kruskal
edges.sort()

# Inisialisasi list untuk menampung jalur MST dan variabel total bobot
mst = []
total_weight = 0

# Set untuk melacak node mana saja yang sudah terhubung ke dalam MST
connected = set()

# Iterasi melalui setiap edge yang sudah terurut
for weight, u, v in edges:

    # Logika pengecekan: Jika salah satu atau kedua node belum masuk ke dalam set connected
    # Catatan: Logika ini efektif untuk graph sederhana, namun pada graph kompleks 
    # biasanya menggunakan struktur data 'Disjoint Set Union' (DSU) untuk mencegah cycle.
    if u not in connected or v not in connected:

        # Menambahkan edge terpilih ke dalam list MST
        mst.append((u, v, weight))
        
        # Menambahkan bobot edge ke total keseluruhan
        total_weight += weight

        # Memasukkan node u dan v ke dalam set node yang sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil akhir
print("Minimum Spanning Tree:")

# Loop untuk mencetak setiap pasangan node dan bobot dalam MST
for edge in mst:
    print(edge)

# Menampilkan jumlah total bobot dari pohon merentang minimum tersebut
print("Total bobot =", total_weight)