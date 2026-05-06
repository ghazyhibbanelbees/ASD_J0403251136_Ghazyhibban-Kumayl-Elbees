#======================================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas: B1
#======================================================
# Latihan 4: Jalur Terpendek Antar Lokasi Kampus
#======================================================

import heapq

# REPRESENTASI DENAH KAMPUS (Bobot angka menunjukkan estimasi waktu dalam menit)
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra_kampus(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# Mencari jalur terpendek dari Gerbang
hasil = dijkstra_kampus(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(f"{lokasi} = {jarak} menit")

# ==============================================================================
# JAWABAN ANALISIS LATIHAN 4:
# 1. Lokasi mana yang paling dekat dari Gerbang? Jawaban: Kantin (2 menit).
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? Jawaban: 7 menit (Gerbang-Kantin-Lab-Aula).
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jawaban: Tidak, 
#    jalur memutar seringkali memiliki total bobot yang lebih rendah.
# 4. Dijkstra cocok untuk kampus karena waktu tempuh antar gedung selalu bernilai positif.
# ==============================================================================