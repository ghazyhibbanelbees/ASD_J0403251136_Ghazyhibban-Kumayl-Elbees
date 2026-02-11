class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.") 
            return False
        
        temp = self.head
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.") 
                return True
            temp = temp.next
            if temp == self.head:
                break
        
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.") 
        return False

cll = CircularSinglyLinkedList()

elemen_input = [3, 7, 12, 19, 25]
for e in elemen_input:
    cll.insert_at_end(e)

print("masukkan elemen yang ingin dicari: 12")
cll.search(12) 