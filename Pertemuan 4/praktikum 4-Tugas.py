# =================================================================
# Nama : Ghazyhibban Kumayl Elbees
# Nim  : J0403251136
# Kelas: B1
# =================================================================

# 1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nomor_antrian, nama_pelanggan, jenis_servis):
        self.nomor_antrian = nomor_antrian  # Menyimpan nomor antrian
        self.nama_pelanggan = nama_pelanggan  # Menyimpan nama pelanggan
        self.jenis_servis = jenis_servis      # Menyimpan jenis servis
        self.next = None                      # Pointer ke node berikutnya

# 2) Mendefinisikan Queue Bengkel
class QueueBengkel:
    def __init__(self):
        # Inisialisasi awal, antrian kosong
        self.front = None
        self.rear = None

    def is_empty(self):
        # Mengecek apakah antrian kosong
        return self.front is None

    # Enqueue: Menambahkan pelanggan ke antrian paling belakang (rear)
    def enqueue(self, nomor, nama, servis):
        new_node = Node(nomor, nama, servis)
        
        # Jika antrian kosong, node baru menjadi front sekaligus rear
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            # Jika tidak kosong, sambungkan node terakhir ke node baru
            self.rear.next = new_node
            # Pindahkan pointer rear ke node yang baru ditambahkan
            self.rear = new_node
        print(f"Pelanggan {nama} berhasil ditambahkan ke antrian.")

    # Dequeue: Melayani pelanggan paling depan (front) sesuai prinsip FIFO
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong! Tidak ada pelanggan untuk dilayani.")
            return None
        
        # Simpan data front yang akan dihapus/dilayani
        node_dilayani = self.front
        
        # Geser pointer front ke node selanjutnya
        self.front = self.front.next
        
        # Jika setelah digeser front menjadi None, maka rear juga harus None
        if self.front is None:
            self.rear = None
            
        return node_dilayani

    # Traversal: Menampilkan seluruh data dalam antrian
    def tampilkan_antrian(self):
        if self.is_empty():
            print("Antrian saat ini kosong.")
            return

        print("\n--- Daftar Antrian Pelanggan (Front -> Rear) ---")
        current = self.front
        i = 1
        while current is not None:
            print(f"{i}. [{current.nomor_antrian}] {current.nama_pelanggan} - {current.jenis_servis}")
            current = current.next
            i += 1
        print("----------------------------------------------")

# 3) Program Utama (Menu)
def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nomor = input("Masukkan Nomor Antrian: ")
            nama = input("Masukkan Nama Pelanggan: ")
            servis = input("Masukkan Jenis Servis: ")
            q.enqueue(nomor, nama, servis)

        elif pilihan == "2":
            pelanggan = q.dequeue()
            if pelanggan:
                print(f"Melayani Pelanggan: [{pelanggan.nomor_antrian}] {pelanggan.nama_pelanggan}")
                print(f"Jenis Servis: {pelanggan.jenis_servis}")

        elif pilihan == "3":
            q.tampilkan_antrian()

        elif pilihan == "4":
            print("Program Selesai. Terima Kasih!")
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1-4.")

# Menjalankan program utama
if __name__ == "__main__":
    main()