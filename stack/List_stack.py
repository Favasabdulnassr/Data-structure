
class Stack:
    def __init__(self) -> None:
        self.new = []

    def push(self,data):
        self.new.append(data) 

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:    
            return self.new.pop()  

    def size(self):
        print(len(self.new))

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else: 
            print(self.new[-1])    

    def is_empty(self):
        return len(self.new) == 0
    

stack = Stack()   

stack.push(1)
stack.push(2)
stack.push(3)

stack.pop()

stack.push(4)

stack.size()

stack.peek

print(stack.new)

        