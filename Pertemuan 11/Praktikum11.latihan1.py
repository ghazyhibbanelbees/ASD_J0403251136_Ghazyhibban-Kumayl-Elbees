from collections import deque

# Representasi Graph hubungan antar lokasi
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')


#JAWABAN:

#1. Node mana yang dikunjungi pertama?
   #Jawaban: Node yang dikunjungi pertama adalah "Rumah", karena dalam kode 
   #tersebut fungsi bfs dipanggil dengan argumen start='Rumah'.

#2. Mengapa BFS cocok untuk mencari jalur terdekat?
   #Jawaban: BFS (Breadth-First Search) menjelajahi graph secara "melebar" 
   #level demi level. Artinya, ia akan memeriksa semua tetangga langsung (jarak 1) 
   #sebelum pindah ke tetangga dari tetangga (jarak 2). Hal ini menjamin bahwa 
   #saat sebuah node target ditemukan, jalur yang diambil adalah jalur dengan 
   #jumlah lompatan (edges) paling sedikit dari titik awal.

#3. Apa perbedaan urutan BFS jika struktur graph diubah?
   #Jawaban: Urutan kunjungan sangat bergantung pada struktur graph (hubungan antar node). 
   #- Jika kita menambah hubungan baru, misalnya dari 'Rumah' langsung ke 'Pasar', 
    # maka 'Pasar' akan dikunjungi lebih awal (pada level 1).
   #- Jika arah panah diubah atau urutan list tetangga dalam dictionary ditukar, 
    # maka urutan node yang masuk ke dalam antrean (queue) juga akan berubah, 
     #sehingga urutan output print-nya pun berbeda.