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
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next_node

    def index_by_delete(self,index):
       
        if index == 0:
            self.head = self.head.next_node
            return
        
        temp = self.head
        count = 0

        while temp is not None and count < index-1:
            temp = temp.next_node
            count += 1
    

        if temp is None or index < 0:
            print(f"index {index} is out of range") 
            return  

        temp.next_node = temp.next_node.next_node    

        return     
    
list = Linkedlist()

list.append(1)
list.append(2)
list.append(3)

list.index_by_delete(2)
list.display()
