# ============================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
# ============================================
# Latihan 1: Graph III: Spanning Tree
# ============================================

# 1. Menyiapkan daftar edge sesuai gambar (A-B, A-C, A-D, C-D, B-D)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# 2. Menyiapkan contoh spanning tree yang valid (terhubung tanpa cycle)
# Sesuai contoh modul: (A, C), (C, D), (D, B)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# 3. Menampilkan daftar edge pada graph awal
print("Edge pada graph:")
for edge in edges:
    print(edge)

# 4. Menampilkan contoh spanning tree yang valid
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 5. Menampilkan jumlah edge pada masing-masing struktur
print(f"\nJumlah edge graph = {len(edges)}")
print(f"Jumlah edge spanning tree = {len(spanning_tree)}")

# ==============================================================================
# Jawaban Analisis:
# ==============================================================================

# 1. Apa perbedaan graph awal dan spanning tree?
# Jawaban: Graph awal adalah graf induk yang dapat memiliki cycle (lintasan tertutup), 
# sedangkan spanning tree adalah subgraf yang menghubungkan semua vertex tanpa cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Jawaban: Karena secara definisi, "Tree" (pohon) harus bersifat acyclic (tidak 
# memiliki sirkuit). Jika ada cycle, maka koneksi tersebut memiliki redundansi.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jawaban: Karena spanning tree hanya menggunakan jumlah minimum edge untuk 
# menghubungkan semua simpul. Jika ada n simpul, jumlah edge adalah n - 1.