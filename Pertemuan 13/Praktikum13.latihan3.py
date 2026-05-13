# ====================================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
# ====================================================
# Latihan 3: Implementasi Algoritma Prim
# ====================================================

import heapq

# Representasi Graph menggunakan Adjacency List (Dictionary)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Set untuk mencatat node yang sudah dikunjungi agar tidak terjadi looping
    visited = set([start])
    
    # Priority Queue (Heap) untuk menyimpan list edge yang bisa diambil. 
    # Format: (bobot, node_asal, node_tujuan). heapq selalu mengambil bobot terkecil.
    edges = []
    
    # Masukkan semua tetangga dari node awal ke dalam priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []           # List untuk menyimpan edge yang terpilih menjadi MST
    total_weight = 0   # Variabel untuk menjumlahkan total bobot MST
    
    # Selama masih ada edge yang bisa dieksplorasi
    while edges:
        # Ambil edge dengan bobot terkecil menggunakan heappop
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan (v) belum pernah dikunjungi
        if v not in visited:
            visited.add(v)                  # Tandai sebagai sudah dikunjungi
            mst.append((u, v, weight))      # Masukkan ke dalam daftar MST
            total_weight += weight          # Tambahkan bobotnya ke total
            
            # Lihat tetangga dari node yang baru saja dikunjungi (v)
            for neighbor, w in graph[v].items():
                # Jika tetangganya belum dikunjungi, masukkan ke antrean (heap)
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan fungsi dengan titik awal node 'A'
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} dengan bobot {edge[2]}")

print("Total bobot =", total)

# =================================================================
# JAWABAN ANALISIS:
# =================================================================
# 1. Node awal apa yang digunakan?
#    Jawaban: Node 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Jawaban: Edge ('A', 'C') dengan bobot 2, karena merupakan bobot 
#    terkecil yang terhubung dengan node 'A'.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Jawaban: Dengan memilih edge dengan bobot terkecil dari kumpulan 
#    edge yang menghubungkan node yang sudah dikunjungi (dalam set visited) 
#    ke node yang belum dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Jawaban: 6.
#    Proses: A-C (2) -> C-D (1) -> D-B (3). Total = 2 + 1 + 3 = 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Jawaban: Prim membangun pohon dari satu titik (node-based) dan 
#    selalu terhubung sejak awal. Kruskal mengumpulkan edge terkecil 
#    di seluruh graph (edge-based) dan menggabungkan komponen-komponen 
#    terpisah hingga menjadi satu pohon.
# =================================================================