class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self,max_length=5):
        self.max_length = max_length
        self.length = 0
        self.table = [None] * max_length

    def hash_fun(self,key):
        return hash(key) % self.max_length

    def insert(self,key,value):
        index = self.hash_fun(key)

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