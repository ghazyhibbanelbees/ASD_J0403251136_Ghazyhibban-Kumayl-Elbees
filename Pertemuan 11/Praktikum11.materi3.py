#===============================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#===============================================

#===============================================
#Implementasi DFS
#===============================================


#representasi graph
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

def dfs(graph,node,visited):
#fungsi untuk melakukan penelusuran graph menggunakan DFS
#graph : dictionary yang menyimpan graph
#node : menyimpan node yang sedang dikunjungi
#visited : menyimpan node yanf sudah dikunjungi

    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        
        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

#set visited 
visited = set()

#menjalankan dfs dari A
dfs(graph, "A", visited)