class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.next = None
 

class Hashtable:
    def __init__(self,max_length=5) -> None:
        self.max_length = max_length
        self.length = 0
        self.table = [None] * max_length

    def _hash(self,key):
        return hash(key) % self.max_length

    def insert(self,key,value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key,value)
            self.length += 1
        else:
            current = self.table[index]

            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            new_node = Node(key,value) 
            new_node.next = self.table[index]
            self.table[index] = new_node   
            self.length += 1

    def search(self,key):
        index = self._hash(key)

        current = self.table[index]  

        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)  
    
  
    
    def remove(self,key):
        index = self._hash(key)
        prev = None
        current = self.table[index] 

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                    self.length -= 1
                    return
                else:
                    self.table[index] = current.next
                    self.length -= 1
                    return

            prev = current
            current = current.next   
        raise KeyError(key)    

    def _length(self):
        return self.length  
    
    def display(self):
        for index, node in enumerate(self.table):
            if node:
                print(f"Index {index}: {node.key}: {node.value}")
                current = node.next
                while current:
                    print(f"Index {index}: {current.key} : {current.value}")
                    current = current.next
        return
            

    

hashtable = Hashtable()

hashtable.insert('favas',1)
hashtable.insert('saban',2)
hashtable.insert('fayis',3)
hashtable.insert('siyaf',4)
hashtable.insert('jabbar',6)
hashtable.insert('salman',7)
hashtable.insert('sulaiman',8)







hashtable.display()


print(hashtable._length())



    