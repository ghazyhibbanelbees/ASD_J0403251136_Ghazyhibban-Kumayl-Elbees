#======================================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas: B1
#======================================================
# Latihan 3: Algoritma Bellman Ford
#======================================================

# REPRESENTASI GRAF DENGAN BOBOT NEGATIF
# Bellman-Ford dapat menangani bobot negatif seperti rute C ke B (-2)
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Bellman-Ford yang mampu menangani bobot negatif.
    """
    
    # Inisialisasi awal: Jarak ke semua node disetel tak hingga, kecuali start=0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 
    
    # Relaksasi berulang: Dilakukan sebanyak (jumlah_node - 1) kali
    for _ in range(len(graph) - 1):
        # Periksa setiap edge (sisi) dalam graf
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak asal sudah diketahui (bukan inf)
                # DAN ditemukan jalur yang lebih kecil ke node tetangga
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    # Update (relaksasi) jarak ke node tetangga tersebut
                    distances[neighbor] = distances[node] + weight
                    
    return distances # Mengembalikan hasil jarak terpendek akhir

# Menjalankan program dimulai dari titik 'A'
hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"{node} = {distance}")

# ==============================================================================
# JAWABAN ANALISIS LATIHAN 3:
# 1. Berapa bobot langsung dari A ke B? Jawaban: 5.
# 2. Berapa total bobot jalur A -> C -> B? Jawaban: 2 (4 + (-2)).
# 3. Jalur mana yang dipilih sebagai jarak terpendek menuju B? Jawaban: A -> C -> B.
# 4. Bellman-Ford dapat digunakan pada graf dengan bobot negatif karena melakukan relaksasi berulang.
# 5. Relaksasi edge: Memperbarui jarak node jika ditemukan jalur baru yang lebih murah.
# 6. Perbedaan utama: Dijkstra lebih cepat namun hanya untuk bobot positif; 
#    Bellman-Ford lebih lambat namun bisa menangani bobot negatif.
# ==============================================================================