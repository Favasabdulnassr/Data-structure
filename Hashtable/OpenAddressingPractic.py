class HashTable:
    def __init__(self,max_size=5):
        self.size = max_size
        self.table = [None] * self.size
        self.count = 0
        self.removed = object()

    def _hash(self,key):
        return hash(key) % self.size
    
    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None]*self.size
        self.count = 0

        for entry in old_table:
            if entry and entry is not self.removed:
                self.insert(entry[0],entry[1])

    def probing(self,index,key):
        start_index = index

        while self.table[index] is not None:
            if self.table[index] is self.removed:
                return index
            if self.table[index][0] == key:
                self.count -= 1
                return index

            index = (index + 1) % self.size

            if index == start_index:
                raise Exception("Hash table is full")

        return index                

    def insert(self,key,value):
        index = self._hash(key)

        if self.count / self.size >= 0.7:
            self.resize()

        if self.table[index] is not None or self.table[index] is self.removed:
            self.table[index] = (key,value)
            self.count += 1
        else:
            if self.table[index][0] == key:
                self.table[index] = (key,value)
                return
            index = self.probing(index,key)
            self.table[index] = (key,value)
            self.count += 1
            return
        
    def search(self,key):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key and self.table[index] is not self.removed:
                return self.table[index][1]
            index = (index + 1) % self.size

            if index == original_index:
                break

        raise KeyError(key)

    def remove(self,key):
        index = self._hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key and self.table[index] is not self.removed:
                self.table[index] = self.removed
                return

            index = (index +1) % self.size

            if index == start_index:
                break

        raise KeyError(key)
           
    
    def length(self):
        return self.count
    

    def display(self):
        for node in self.table:
            if node and node is not self.removed:
                print(node[0],node[1])
                
        return
            
        
                

                        

