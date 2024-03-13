class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self,max_length=6) -> None:
        self.max_length = max_length
        self.size = 0
        self.table = [None] * max_length

    def hash_fun(self,key):
        return hash(key) % self.max_length
    
    def insert(self,key,value):
        index = self.hash_fun(key)

        if self.table[index] is None:
            self.table[index] = Node(key,value)
            self.size += 1
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
            self.size += 1

    def search(self,key):
        index = self.hash_fun(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)    
    
    def remove(self,key):
        index = self.hash_fun(key)
        prev = None
        current = self.table[index]

        while current:
            if prev:
                if current.key == key:
                    prev.next = current.next
                    self.size -= 1
                    return
            else:
                if current.key == key:
                    self.table[index] = current.next
                    self.size -= 1

            prev = current
            current = current.next

        raise KeyError(key)    

    def length(self):
        return self.size     

    def display(self):
        for i in self.table:
            if i:
                print(i.key,i.value)
                j = i.next    
                while j:
                    print(j.key,j.value)
                    j = j.next
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


                
