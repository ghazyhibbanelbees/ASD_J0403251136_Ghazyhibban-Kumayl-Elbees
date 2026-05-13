# ====================================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
# ====================================================
# Latihan 2: Implementasi Sederhana Algoritma Kruskal
# ====================================================

# Daftar edge dengan format: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil (Greedy Approach)
edges.sort()

mst = []
total_weight = 0

connected = set()

print("Proses Pemilihan Edge (Kruskal):")
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    # Logika sederhana: setidaknya salah satu node belum terhubung
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        
        # Tambahkan node ke set connected
        connected.add(u)
        connected.add(v)
        print(f"Dipilih: {u}-{v} dengan bobot {weight}")
    else:
        print(f"Dilewati: {u}-{v} dengan bobot {weight} (Potensi Cycle)")

# Menampilkan hasil akhir
print("\nMinimum Spanning Tree:")
for edge in mst:
    print(edge)

print(f"Total bobot = {total_weight}")

# ==============================================================================
# Jawaban Analisis:
# ==============================================================================

# 1. Edge mana yang dipilih pertama kali?
# Jawaban: Edge ('C', 'D') dengan bobot 1. Karena algoritma Kruskal selalu 
# memulai dengan mengurutkan bobot dari yang terkecil dan memilih yang paling minimal.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Jawaban: Karena Kruskal adalah algoritma "Greedy" yang bertujuan mencari 
# "Minimum" Spanning Tree. Memilih bobot terkecil di setiap langkah adalah strategi 
# untuk mendapatkan total bobot keseluruhan yang paling rendah.

# 3. Berapa total bobot MST yang dihasilkan?
# Jawaban: Total bobotnya adalah 6. 
# Berasal dari: (C-D: 1) + (A-C: 2) + (B-D: 3) = 6.

# 4. Mengapa edge tertentu tidak dipilih?
# Jawaban: Karena edge tersebut menghubungkan dua simpul yang keduanya sudah 
# masuk ke dalam struktur pohon (sudah ada di set 'connected'). Jika tetap 
# dipilih, maka akan terbentuk cycle (sirkuit), yang melanggar aturan Spanning Tree.
# Contoh pada kode ini: Edge (A, B) bobot 4 dan (A, D) bobot 5 tidak dipilih.