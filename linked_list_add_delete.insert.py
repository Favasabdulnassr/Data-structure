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

    def delete(self,data):
        temp = self.head

        if temp != None and temp.data == data:
            self.head = temp.next_node
            return
        
        while temp != None and data != temp.data:
            prev = temp
            temp = temp.next_node

        if temp == None:
            return     

        if temp == self.tail:
            self.tail = prev
            self.tail.next_node = None
            return

        else:
            prev.next_node = temp.next_node
                

    def insert(self,before_data,data):
        new_node = Node(data)
        temp = self.head

        while temp != None and temp.data != before_data:
            temp = temp.next_node

        if temp.data == before_data and temp.data != self.tail:
            new_node.next_node =  temp.next_node
            temp.next_node     = new_node
            new_node.data = new_node.data
            return 
            

        elif temp.data == self.tail:
            temp.next_node = new_node
            new_node.data = new_node

        else:
            return
            
    def display(self):  
        current_node = self.head
        
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
         
linkedlist = Linkedlist()       

linkedlist.append(5)
linkedlist.append(6)
linkedlist.append(7)

linkedlist.delete(7)
linkedlist.insert(5,7)
linkedlist.insert(6,8)
linkedlist.insert()
linkedlist.display()

