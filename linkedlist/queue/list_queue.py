class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self,data):
        self.items.append(data)
        return
    
    def dequeue(self):
        self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0]
    
    def rear(self):
        return self.rear[-1]
    
    def display(self):
        for item in self.items:
            print(item,end="  ")
        print()    

queue = Queue()

queue.enqueue(13)
queue.enqueue(31)
queue.enqueue(15)
queue.enqueue(17)
queue.enqueue(19)
queue.enqueue(3)
queue.enqueue(2)

queue.dequeue()

queue.display()

    