# ====================================================
# Nama : Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
# ====================================================
# Latihan 4: Studi Kasus: Jaringan Kabel Antar Gedung
# ====================================================

import heapq

graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungB': 3, 'GedungC': 1, 'GedungA': 5}
}

def prim_jaringan_kabel(graph, start_node):
    # Inisialisasi
    visited = set([start_node])
    edges = []
    
    # Masukkan semua jalur dari gedung awal ke antrean prioritas (heap)
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))
        
    mst = []           # Menyimpan edge yang dipilih
    total_cost = 0     # Menyimpan total biaya minimum
    
    # 2. IMPLEMENTASI ALGORITMA PRIM
    while edges:
        # Ambil jalur dengan biaya (weight) terendah
        weight, u, v = heapq.heappop(edges)
        
        # Jika gedung tujuan belum terhubung ke jaringan
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight
            
            # Tambahkan semua jalur dari gedung yang baru terhubung
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_cost

# Eksekusi Program
gedung_awal = 'GedungA'
jalur_terpilih, biaya_total = prim_jaringan_kabel(graph, gedung_awal)

# 3. OUTPUT EDGE YANG DIPILIH
print("=== Rencana Pemasangan Jaringan Kabel ===")
for u, v, w in jalur_terpilih:
    print(f"Hubungkan {u} ke {v} dengan biaya: {w}")

# 4. OUTPUT TOTAL BIAYA MINIMUM
print("-" * 40)
print(f"Total Biaya Minimum Pemasangan: {biaya_total}")
print("-" * 40)

# =================================================================
# JAWABAN ANALISIS (Dalam Komentar):
# =================================================================
# # 1. Algoritma apa yang digunakan?
# #    Jawaban: Algoritma Prim. Algoritma ini dipilih karena efektif untuk 
# #    membangun jaringan dari satu titik awal dan menjamin biaya minimum.
#
# # 2. Edge mana saja yang dipilih?
# #    Jawaban: 
# #    - GedungA ke GedungC (Biaya 2)
# #    - GedungC ke GedungD (Biaya 1)
# #    - GedungD ke GedungB (Biaya 3)
#
# # 3. Berapa total biaya minimum?
# #    Jawaban: 6 (2 + 1 + 3 = 6).
#
# # 4. Mengapa MST cocok digunakan pada kasus ini?
# #    Jawaban: Karena tujuan kasus ini adalah menghubungkan seluruh gedung 
# #    (semua node) sehingga saling terhubung tanpa ada gedung yang terisolasi, 
# #    namun dengan batasan biaya serendah mungkin (minimum cost) dan 
# #    menghindari adanya jalur ganda yang sia-sia (siklus/loop).
# =================================================================