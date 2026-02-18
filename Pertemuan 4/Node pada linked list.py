#==========================================
#Nama : Ghazyhibban Kumayl elbees
#NIM : J0403251136
#Kelas : B1
#==========================================
#Implementasi Dasar: Node pada Linked List
#==========================================
#Membuat class Node (unit dasar dari linked list)
class Node:
    def __init__(self, data): #fungsi konstruktor (otomatis dijalankan saat class di connect kan ke suatu objek)
        self.data = data #menyimpan data
        self.next = None #pointer ke node berikutnya

# 1)Membuat node satu persatu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Siapa head nya
head = nodeA

# 4) Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)
    current = current.next

#===============================================
#Implementasi Dasar : Linked List + Insert Awal
#===============================================

class LinkedList:
    def __init__(self):
        self.head = None #awalnya kosong


    def insert_awal(self,data): #push dalam stack
        #1) buat node baru
        nodeBaru = Node(data) #panggil class node

        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3) head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data  #peek (melihat head) dalam stack 
        #geser head ke node berikutnya
        self.head = self.head.next
        print("Node yang terhapus: ", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print (current.data)
            current = current.next

print("===================List Baru=====================")
ll = LinkedList() #instantiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
print("===================List Baru=====================")
ll.hapus_awal()
ll.tampilkan()