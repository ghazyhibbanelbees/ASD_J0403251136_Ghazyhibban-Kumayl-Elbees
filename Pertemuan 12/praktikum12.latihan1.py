#======================================================
# Nama: Ghazyhibban Kumayl Elbees
# NIM : J0403251136
# Kelas: B1
#======================================================
# Latihan 1: Weighted Graph dan Shortest Path Sederhana
#======================================================

# 1. REPRESENTASI GRAF
# Kita menggunakan 'Nested Dictionary' (Dictionary di dalam Dictionary).
# Key utama adalah nama Node, dan valuenya adalah dictionary berisi tetangga serta bobotnya.
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B (bobot 4) dan ke C (bobot 2)
    'B': {'D': 5},           # Node B hanya terhubung ke D (bobot 5)
    'C': {'D': 1},           # Node C hanya terhubung ke D (bobot 1)
    'D': {}                  # Node D adalah node tujuan/akhir (tidak punya tetangga keluar)
}

# 2. PERHITUNGAN JALUR SECARA MANUAL
# Di sini kita mengakses nilai bobot dengan cara memanggil key-nya: graph[Asal][Tujuan]

# Menghitung total biaya Jalur 1 (A -> B -> D)
# Kita mengambil bobot dari A ke B, lalu menambahkannya dengan bobot dari B ke D.
jalur_1 = graph['A']['B'] + graph['B']['D']  # Hasil: 4 + 5 = 9

# Menghitung total biaya Jalur 2 (A -> C -> D)
# Kita mengambil bobot dari A ke C, lalu menambahkannya dengan bobot dari C ke D.
jalur_2 = graph['A']['C'] + graph['C']['D']  # Hasil: 2 + 1 = 3

# 3. OUTPUT HASIL PERHITUNGAN
print(f"Total biaya Jalur 1 (A ke B ke D) adalah: {jalur_1}")
print(f"Total biaya Jalur 2 (A ke C ke D) adalah: {jalur_2}")

# 4. LOGIKA PENGAMBILAN KEPUTUSAN (KONDISIONAL)
# Algoritma Shortest Path selalu mencari nilai yang paling minimum.
if jalur_1 < jalur_2:
    # Jika jalur_1 lebih kecil, maka jalur_1 yang terbaik.
    print("Keputusan: Jalur terpendek adalah A -> B -> D")
else:
    # Karena jalur_2 (3) lebih kecil dari jalur_1 (9), maka blok ini yang akan dieksekusi.
    print("Keputusan: Jalur terpendek adalah A -> C -> D")

# ==============================================================================
# JAWABAN ANALISIS (UNTUK LAPORAN PRAKTIKUM)
# ==============================================================================

#1. Berapa total bobot jalur A -> B -> D? 
#   Jawaban: 9.
#
#2. Berapa total bobot jalur A -> C -> D? 
#   Jawaban: 3.
#
#3. Jalur mana yang dipilih sebagai jalur terpendek? 
#   Jawaban: Jalur A -> C -> D, karena memiliki total bobot paling rendah.
#
#4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit? 
#   Jawaban: Karena pada graf berbobot, setiap jalur (edge) memiliki 'biaya' yang berbeda. 
#   Sebuah jalur yang terlihat 'pendek' (misal: hanya 1 lompatan) bisa jadi sangat mahal 
#  dibandingkan jalur yang 'memutar' (misal: 3 lompatan) tetapi memiliki bobot yang kecil. 
#   Inti dari algoritma ini adalah efisiensi biaya/waktu, bukan sekadar jumlah langkah.
