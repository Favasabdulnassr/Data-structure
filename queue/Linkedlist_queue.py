
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self,data):
        new_data = Node(data)

        if self.rear is None:
            self.front = self.rear = new_data
            return
        else:
            self.rear.next = new_data
            self.rear = new_data  
            return  

    def dequeue(self):
        if self.is_empty():
            return None
        
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None

        return    
    
    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count    
    
    def display(self):
        current = self.front
        while current:
            print(current.data,end="  ")
            current = current.next
        print()   

   

    
queue = Queue()


queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(2)
queue.enqueue(19)
queue.enqueue(12)

queue.dequeue()

print(queue.front.data)

print(queue.rear.data)

print(queue.size())

queue.display()

