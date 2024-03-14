from collections import deque

class Queue:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return print(len(self.items))

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return print(self.items[0])      

    def display(self):
        for  item in self.items:
            print(item)     

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(14)
queue.enqueue(12)
queue.enqueue(16)

queue.dequeue()

queue.front()

print(queue.is_empty())

queue.size()


queue.display()


