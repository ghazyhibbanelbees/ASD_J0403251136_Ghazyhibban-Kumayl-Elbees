#======================================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas: B1
#======================================================
# Latihan 2: Algoritma Dijkstra
#======================================================

import heapq # Mengimpor library heapq untuk mengelola priority queue agar pencarian jarak terkecil lebih efisien

# Menggunakan nested dictionary: key pertama adalah node asal, key kedua adalah tetangga dan bobotnya
graph = {
    'A': {'B': 4, 'C': 2}, # Node A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},          # Node B terhubung ke D (bobot 5)
    'C': {'D': 1},          # Node C terhubung ke D (bobot 1)
    'D': {}                 # Node D tidak memiliki tetangga keluar
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Dijkstra yang efisien untuk bobot positif.
    """
    
    # Inisialisasi: Semua jarak awal ke setiap node dianggap tak hingga (inf)
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari titik mulai ke dirinya sendiri selalu disetel 0
    distances[start] = 0
    
    # Priority queue menyimpan pasangan (jarak, node). Dimulai dengan node awal.
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Mengambil node dengan jarak terkecil dari antrean prioritas
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, abaikan proses ini
        if current_distance > distances[current_node]:
            continue
            
        # Memeriksa semua tetangga dari node yang sedang diproses saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak baru: jarak saat ini + bobot menuju tetangga
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih kecil/pendek dari yang sudah tercatat
            if distance < distances[neighbor]:
                # Perbarui catatan jarak minimum untuk node tetangga tersebut
                distances[neighbor] = distance
                # Masukkan tetangga dan jarak barunya ke priority queue untuk dicek nanti
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances # Mengembalikan hasil akhir berupa dictionary jarak terpendek

# Memanggil fungsi dimulai dari node 'A'
hasil = dijkstra(graph, 'A')

# Mencetak output jarak dari node A ke setiap node lainnya
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"{node} = {distance}")

# ==============================================================================
# JAWABAN ANALISIS LATIHAN 2:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3.
# 4. Jarak A ke D (3) lebih kecil melalui C dibandingkan melalui B (4+5=9).
# 5. Fungsi priority_queue: Mengambil node dengan bobot terkecil untuk diproses lebih dulu.
# 6. Dijkstra tidak cocok untuk graf berbobot negatif karena algoritma ini menganggap 
#    sekali node dikunjungi, jaraknya sudah paling minimal (final).
# ==============================================================================