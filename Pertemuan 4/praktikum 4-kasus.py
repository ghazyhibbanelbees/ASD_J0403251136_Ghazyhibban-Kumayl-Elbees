#=================================================================
#Nama : Ghazyhibban Kumayl Elbees
#Nim : J0403251136
#Kelas : B1
#=================================================================

#=================================================================
#Studi Kasus : Sistem Layanan Akademik
#Implementasi Queue =>
#Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue memindahkan pointer front (menghapus data dari depan)
# Front ->  A > B ->Rear
#=================================================================

#1) Mendefinisikan Node (Unit dasae linked list)
class Node:
    def _init_(self, nim, nama):
       self.nim    #menyimpan NIM mahasiswa
       self.nama   #menyiman Nama mahasiswa
       self.next   #pointer ke node berikutnya

#2)Mendefinisikan queue, terdiri dari font dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_Empty(self):
        #Ketika queue kosong maka front = rear = none
        return self.front is None

#menambahkan data baru ke bagian belakang (rear)    
    def enqueue(self, nim, nama):
        NodeBaru = Node(nim, nama) #instansi
        #Jika data baru nmasuk dari queue yang kosong maka data baru = dront = rear
        if self.is_empty():
            self.front = NodeBaru
            self.rear = NodeBaru
            return
        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear   
        NodeBaru = Node(nim, nama)
        self.rear.next = NodeBaru
        self.rear = NodeBaru

    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_Empty():
            print("Antrian kosong, Tdak ada mahasiswa yang dilayani")
            return None
        
        #lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        #geser ointer front ke nexr front
        self.front = self.front.next

        #jika front menjadi none(data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear=None
 
        return node_dilayani
    
    def tampilkan(self):



        print("Daftar Antrian Mahasiswa (front -> rear: ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no =+ 1

#Program Utama

def main():

    #instantiasi queueu
    q = queueAkademik()

    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4) : ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM :").strip()
            nama = input("Masukkan Nama : ").strip()

            q.enqueue(nim, nama)
            print("Mahasiswa Berhasil Ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Diloayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program Selesai. Terima Kasih")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")

#penanda eksekusi file utama
if __name__ == "__main__":
    print = main()