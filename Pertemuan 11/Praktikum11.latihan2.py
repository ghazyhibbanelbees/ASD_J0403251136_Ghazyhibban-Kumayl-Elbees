# Graph berikut mempresentasikan jalur eksplorasia:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Gunakan algoritma DFS untuk menelusuri graph mulai dari node A.
def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)


#JAWABAN:

#1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
   #Jawaban: DFS (Depth-First Search) menggunakan prinsip tumpukan (stack), 
   #baik secara eksplisit maupun implisit melalui rekursi. Saat mengunjungi 
   #suatu node, algoritma ini langsung "menyelam" ke tetangga pertama yang 
   #ditemukan sebelum kembali (backtrack) untuk memeriksa tetangga lainnya 
   #di level yang sama. Itulah sebabnya ia disebut penelusuran "mendalam".

#2. Apa yang terjadi jika urutan neighbor diubah?
   #Jawaban: Jika urutan neighbor dalam list diubah (misalnya 'A': ['C', 'B']), 
   #maka urutan kunjungan node akan berubah total karena DFS akan memprioritaskan 
   #jalur yang muncul lebih awal di daftar tetangga tersebut. Namun, semua node 
   #yang terhubung tetap akan dikunjungi pada akhirnya.

#3. Bandingkan hasil DFS dengan BFS pada graph yang sama:
   #- Hasil DFS (berdasarkan kode): A -> B -> D -> E -> C -> F 
     #(DFS menelusuri satu cabang sampai mentok baru pindah cabang).
   #- Hasil BFS (jika diterapkan): A -> B -> C -> D -> E -> F 
     #(BFS menelusuri semua tetangga terdekat di level yang sama dulu 
     #sebelum masuk ke level yang lebih dalam).