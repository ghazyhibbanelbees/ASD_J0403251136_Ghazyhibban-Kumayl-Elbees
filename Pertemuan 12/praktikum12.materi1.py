#======================================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas: B1
#======================================================
# Materi 1: Algoritma Dijkstra
#======================================================

import heapq

# Definisi graf menggunakan dictionary (Adjacency List)
# A terhubung ke B (bobot 4) dan C (bobot 2)
# B terhubung ke D (bobot 5)
# C terhubung ke D (bobot 1)
# D tidak memiliki tetangga keluar
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum dari titik awal ke setiap node
    # Inisialisasi awal semua node dengan jarak tak terhingga (infinity)
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan tuple (jarak, node)
    # Dimulai dengan node awal
    pq = [(0, start)]
    
    while pq:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # Periksa semua tetangga dari node yang sedang diproses
        for neighbor, weight in graph[current_node].items():
            
            # Hitung total jarak baru menuju tetangga tersebut
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih pendek dari yang sudah ada sebelumnya
            if distance < distances[neighbor]:
                # Update jarak minimum untuk node tetangga tersebut
                distances[neighbor] = distance
                
                # Masukkan tetangga ke dalam priority queue untuk diperiksa nanti
                heapq.heappush(pq, (distance, neighbor))
                
    # Mengembalikan dictionary berisi jarak terpendek ke semua node
    return distances

# Memanggil fungsi dijkstra dengan titik mulai dari node 'A'
hasil = dijkstra(graph, 'A')

# Mencetak hasil akhir berupa jarak terpendek ke setiap node
print(hasil)
