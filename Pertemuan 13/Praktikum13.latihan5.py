# ====================================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
# ====================================================
# Latihan 5: Buat Program MST dengan kasus baru
# ====================================================

# 1. REPRESENTASI WEIGHTED GRAPH
# Daftar edge: (bobot, node1, node2)
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Helper function untuk mencari root (untuk mendeteksi cycle)
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Helper function untuk menggabungkan dua set
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal_mst(nodes, edge_list):
    # 2. IMPLEMENTASI ALGORITMA KRUSKAL
    # Langkah 1: Urutkan semua edge berdasarkan bobot terkecil
    edge_list.sort()
    
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    mst = []
    total_weight = 0
    
    for weight, u, v in edge_list:
        root_u = find(parent, u)
        root_v = find(parent, v)
        
        # Langkah 2: Jika tidak membentuk cycle, tambahkan ke MST
        if root_u != root_v:
            union(parent, rank, root_u, root_v)
            mst.append((u, v, weight))
            total_weight += weight
            
    return mst, total_weight

# Data Node
nodes = ['RouterA', 'RouterB', 'RouterC', 'RouterD']

# Jalankan Fungsi
mst_result, total_bobot = kruskal_mst(nodes, edges)

# 3. OUTPUT MST
print("=== Minimum Spanning Tree (Kruskal) ===")
for u, v, w in mst_result:
    print(f"Edge: {u} - {v} | Bobot: {w}")

# 4. OUTPUT TOTAL BOBOT MINIMUM
print("-" * 40)
print(f"Total Bobot Minimum: {total_bobot}")
print("-" * 40)

# =================================================================
# JAWABAN ANALISIS:
# =================================================================
# # 1. Kasus apa yang dipilih?
# #    Jawaban: Kasus 2 - Jaringan Komputer (Router).
#
# # 2. Algoritma apa yang digunakan?
# #    Jawaban: Algoritma Kruskal.
#
# # 3. Edge mana saja yang dipilih dalam MST?
# #    Jawaban: 
# #    - RouterC - RouterD (Bobot 1)
# #    - RouterA - RouterC (Bobot 2)
# #    - RouterA - RouterB (Bobot 3)
#
# # 4. Berapa total bobot MST?
# #    Jawaban: 6 (1 + 2 + 3 = 6).
#
# # 5. Mengapa edge tertentu tidak dipilih?
# #    Jawaban: 
# #    - Edge RouterB-RouterC (4) dan RouterB-RouterD (5) tidak dipilih 
# #      karena jika ditambahkan akan membentuk cycle (sirkuit). 
# #      Dalam MST, kita harus menghubungkan semua node tanpa adanya loop 
# #      dan menggunakan total bobot paling kecil.
# =================================================================