class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
        

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self,data):

        new_node = Node(data)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def middlenode(self):
        slow = self.head
        speed = self.head

        while  speed != None and speed.next_node!=None:
            slow  = slow.next_node
            speed = speed.next_node.next_node
        print('middle node',slow.data)
            

    def display(self):

        current_node = self.head

        while current_node:
            print(current_node.data,end=' ---> ')
            current_node = current_node.next_node

list = Linked_list()                

list.append(1)
list.append(2)
list.append(3)
list.middlenode()
list.display()
