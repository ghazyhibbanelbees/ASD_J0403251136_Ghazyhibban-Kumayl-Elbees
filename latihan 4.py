class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if not self.head:
            print("kosong", end="")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null", end="")


def gabungkan_list(list1, list2):

    if not list1.head:
        return list2
    
    if not list2.head:
        return list1

    temp = list1.head
    while temp.next:
        temp = temp.next
    
    temp.next = list2.head
    return list1

ll1 = LinkedList()
for x in [1, 3, 5, 7]: ll1.insert_at_end(x)

ll2 = LinkedList()
for x in [2, 4, 6, 8]: ll2.insert_at_end(x)

print("Linked List 1:", end=" ")
ll1.display()
print("\nLinked List 2:", end=" ")
ll2.display()

list_gabungan = gabungkan_list(ll1, ll2)

print("\nLinked List setelah digabungkan:", end=" ")
list_gabungan.display()