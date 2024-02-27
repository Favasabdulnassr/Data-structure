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
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return  

    def reverse(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node
           
            prev_node = current_node
            current_node = next_node

        self.tail = self.head
        self.head = prev_node

list = Linkedlist()

list.append(1)
list.append(2)
list.append(3)
list.append(4)

list.reverse()
list.display()

        
