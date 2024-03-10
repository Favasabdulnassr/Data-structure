class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node 
            self.tail = new_node

        return
         
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_node
        return      

    def remove_duplicate(self):
        current = self.head
        while current and current.next_node:
            if current.data == current.next_node.data:
                current.next_node = current.next_node.next_node
            else:    
                current = current.next_node
        return

list = Linkedlist ()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(4)
list.append(5)

list.remove_duplicate()

list.display()

