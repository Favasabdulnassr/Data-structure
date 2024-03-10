# array = [1,2,3,4,5,6,7]
# target = -1

# def fun(array,target):
#     low = 0
#     high = len(array)
    
#     while low < high:
#         mid = (low + high)//2
#         mid_element = array[mid]

#         if mid_element == target:
#             return True
#         elif mid_element < target:
#             low = mid
#         elif mid_element > target:
#             high = mid
  
#     return False     

# print(fun(array,target))    

class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

class Linkelist:
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

    def add_end(self,data) :
        new_node = Node(data)
        self.tail.next_node = new_node  
        return  

    def removebeggining(self):
        self.head = self.head.next_node
        return  
    def  display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node  
        return  
    
list = Linkelist()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.add_end(5)
list.removebeggining()
list.display()