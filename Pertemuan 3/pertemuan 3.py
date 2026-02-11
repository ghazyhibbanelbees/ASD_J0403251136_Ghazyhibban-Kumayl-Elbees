class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
        self.prev = None 

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            tail = self.head.prev 
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display_forward(self):
        if not self.head:
            print("List kosong.")
            return
        
        temp = self.head
        print("Traversing forward:")
        while True:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("null")

    def display_backward(self):
        if not self.head:
            print("List kosong.")
            return
        
        tail = self.head.prev
        temp = tail
        print("Traversing backward:")
        while True:
            print(f"{temp.data}", end=" -> ")
            temp = temp.prev
            if temp == tail:
                break
        print("null")

dll = CircularDoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)

dll.display_forward()
dll.display_backward()