from queue import LifoQueue

class Stack:
    def __init__(self) -> None:
        self.items = LifoQueue(maxsize=0)

    def is_empty(self):
        return self.items.empty()
    
    def is_full(self):
        return self.items.full()
    
    def size(self):
        return self.items.qsize()
    
    def push(self,data):
        self.items.put(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack error")
        else:
            self.items.get()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack error")
        else:
            item = self.items.get()
            self.items.put(item)
            return item  
        
    def print_stack(self):
        print(list(self.items.queue))    

stack =Stack()         

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())

stack.pop()

print(stack.size())

print(stack.is_empty())

print(stack.is_full())

stack.print_stack()

