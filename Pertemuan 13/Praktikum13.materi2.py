# =========================================================
# Nama: Ghazyhibban Kumayl Elbees
# Nim: J0403251136
# Kelas: B1
# ==========================================================
# Materi 2: Algoritma Prim
# ==========================================================

import heapq

# Representasi Graph menggunakan Adjacency List (Dictionary dalam Dictionary)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Set untuk melacak node yang sudah masuk ke dalam MST (agar tidak terjadi cycle)
    visited = set([start])

    # List untuk menampung edge yang tersedia (Priority Queue/Min-Heap)
    edges = []

    # Mengambil semua tetangga dari node awal dan memasukkannya ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

        # Inisialisasi penampung hasil MST dan total bobotnya
        mst = []
        total_weight = 0

        # Melakukan iterasi selama masih ada edge yang bisa dieksplorasi di heap
        while edges:

            # Mengambil edge dengan bobot terkecil (Greedy Property)
            weight, u, v = heapq.heappop(edges)

            # Jika node tujuan (v) belum dikunjungi, masukkan ke MST
            if v not in visited:

                visited.add(v) # Tandai node sebagai sudah dikunjungi

                mst.append((u, v, weight)) # Tambahkan edge ke hasil akhir
                total_weight += weight # Akumulasi total bobot

                # Periksa semua tetangga dari node yang baru saja dikunjungi
                for neighbor, w in graph[v].items():

                    # Jika tetangga belum dikunjungi, masukkan ke antrean prioritas
                    if neighbor not in visited:
                        heapq.heappush(edges, (w, v, neighbor))

            # Mengembalikan hasil MST dan total bobotnya
            return mst, total_weight
        
# Memanggil fungsi prim dengan node awal 'A'
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

# Menampilkan setiap edge yang terpilih dalam MST
for edge in mst:
    print(edge)
    
# Menampilkan hasil akhir bobot minimum
print("Total bobot =", total)