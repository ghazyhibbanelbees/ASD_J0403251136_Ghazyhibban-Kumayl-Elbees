#==========================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#==========================================
#Implementasi Dasar: Queue
#==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        nodeBaru = Node(data)

        #kalau queue kosong, front dan rear menunjuk ke node yang sama
        if self.front is None:
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self):
        #hapus data dari depan

        #pilih data paling depan
        data_terhapus = self.front.data

        #geser front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus menjadi none
        if self.front is None:
           self.rear = None

        
        print("Data yang terhapus:", data_terhapus)

    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

que = QueueLL()
que.enqueue("A")
que.enqueue("B")
que.enqueue("C")
que.tampilkan()
que.dequeue()
que.tampilkan()