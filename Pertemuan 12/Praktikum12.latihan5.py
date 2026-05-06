#======================================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas: B1
#======================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
#======================================================

import heapq

# 1. REPRESENTASI GRAPH BERBOBOT ANTAR KOTA (Dictionary)
# Data hubungan antar kota sesuai instruksi soal
graph_antar_kota = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. FUNGSI DIJKSTRA
def dijkstra_kota(graph, start):
    # Setel semua jarak kota ke tak terhingga kecuali titik mulai
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue untuk efisiensi pemilihan kota terdekat
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        # Cek setiap tetangga dari kota yang sedang diperiksa
        for neighbor, weight in graph[curr_node].items():
            dist = curr_dist + weight
            # 5. Komentar penjelasan: Jika rute baru ini lebih murah, perbarui datanya
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances

# 3. INPUT NODE AWAL: BOGOR
start_node = 'Bogor'
# 4. OUTPUT JARAK TERPENDEK KE SEMUA NODE
hasil_rute = dijkstra_kota(graph_antar_kota, start_node)

print(f"Jarak terpendek dari {start_node}:")
for kota, jarak in hasil_rute.items():
    print(f"{start_node} -> {kota} = {jarak}")

# ==============================================================================
# JAWABAN ANALISIS LATIHAN 5:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node dengan jarak paling kecil dari Bogor adalah Depok (2).
# 3. Node dengan jarak paling besar dari Bogor adalah Bandung (8).
# 4. Cara kerja: Algoritma mengecek Bogor-Depok (2), lalu Depok-Jakarta (2+2=4), 
#    dan Depok-Bandung (2+6=8). Rute ini lebih efisien dibanding jalur langsung.
# ==============================================================================