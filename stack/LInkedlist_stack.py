class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next_node = None

class Stack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self):
        return self.top == None     

    def push(self,data):
        new_node = Node(data)  
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return print("stack is empty")
        else:
            self.top = self.top.next_node

    def peek(self):
        if self.is_empty():
            return print("stack is empty")
        else:
            return self.top.data       
       
    def size(self):
        if self.is_empty():
            print("empty stack")
        else:
            count = 0
            current = self.top
            while current:
                count += 1
                current = current.next_node
            print(count)   
        
    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next_node


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.size()
print(stack.peek())
stack.display()