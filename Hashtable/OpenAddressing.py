class Hashmap:
    def __init__(self,max_size = 3):
        self.max_size = max_size
        self.table = [None]* max_size
        self.count = 0
        self.removed = object()

    def _hash(self,key):
        return hash(key) % self.max_size
    
    
    def probing(self,index,key):
        start_index = index

        while self.table[index] is not None:
            if self.table[index] is self.removed:
                return index
            
            if self.table[index][0] == key:
                return index
            
            index = (index+1) % self.max_size

            if index == start_index:
                raise Exception("Hash table is full")

        return index
    
    def resize(self):
        old_table = self.table
        self.max_size *= 2
        self.table = [None]*self.max_size
        self.count = 0

        for entry in old_table:
            if entry and entry is not self.removed:
                self.insert(entry[0],entry[1])
    

    def insert(self,key,value):

        if self.count / self.max_size >= 0.7:
            self.resize()
            
        index = self._hash(key)

        if self.table[index] is None or self.table[index] is self.removed:
            self.table[index] = (key,value)
            self.count += 1
        else:
            if self.table[index][0] == key:
                self.table[index] = (key,value)
                return
            index = self.probing(index,key)
            self.table[index] = (key,value)
            self.count += 1

    def search(self,key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key and self.table[index] is not self.removed:
                return self.table[index][1]
            index = (index + 1) % self.max_size

            if index == original_index:
                break

        raise KeyError(key) 

    def remove(self,key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key and self.table[index] is not self.removed:
                self.table[index] = self.removed
                self.count -= 1
                print('removed given key value')
                return
            index = (index + 1) % self.max_size

            if index == original_index:
                break
        
        raise KeyError(key)    

    
    def length(self):
        return self.count
    
    def display(self):
        for index,node in enumerate(self.table):
            if node and node is not self.removed:
                print(f"index : {index}  key : {node[0]}, value : {node[1]}")

        return
            


        



dic = Hashmap()
dic.insert("favas",1)
dic.insert("savaf",3)
dic.remove("favas")
dic.display()
print(dic.length())