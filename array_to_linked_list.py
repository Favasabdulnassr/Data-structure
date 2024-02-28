# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next_node = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next_node = new_node
#             self.tail = new_node

#         return

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next_node
#         return
    
#     def form_to_array(self):
#         new_array = []
#         node = self.head

#         while node:
#             new_array.append(node.data)
#             node = node.next_node
#         return new_array  

# list = Linkedlist()
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)

# print(list.form_to_array())



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

        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def array_to_linkedlist(self,array):
        for item in array:
            self.append(item)

list = Linkedlist()
array = [1,2,3,4,5,6,7,8,9]
list.array_to_linkedlist(array)  
list.display()          

            


