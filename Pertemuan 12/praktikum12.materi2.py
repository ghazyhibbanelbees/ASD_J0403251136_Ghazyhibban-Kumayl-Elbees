#======================================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas: B1
#======================================================
# Materi 2: Algoritma Bellman Ford
#======================================================

def bellman_ford(graph, start):
    # Inisialisasi jarak: setel semua node dengan nilai tak terhingga (inf)
    # kecuali node awal (start) yang disetel ke 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaksasi berulang:
    # Algoritma Bellman-Ford melakukan relaksasi sebanyak (jumlah node - 1) kali
    # Ini menjamin jarak terpendek ditemukan jika tidak ada siklus bobot negatif
    for _ in range(len(graph) - 1):

        # Iterasi melalui setiap node dalam graf
        for node in graph:
            
            # Periksa setiap tetangga (neighbor) dan bobot (weight) dari node tersebut
            for neighbor, weight in graph[node].items():
                
                # Jika jarak ke node asal ditambah bobot menuju tetangga lebih kecil
                # dari jarak yang tersimpan saat ini di node tetangga tersebut
                if distances[node] + weight < distances[neighbor]:
                    
                    # Update (relaksasi) jarak ke node tetangga dengan nilai yang lebih kecil
                    distances[neighbor] = distances[node] + weight

    # Mengembalikan dictionary yang berisi jarak terpendek dari start ke semua node
    return distances
