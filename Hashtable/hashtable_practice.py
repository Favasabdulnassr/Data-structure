class Hashtable:
    def __init__(self,Max_length=5) -> None:
        self.size = 0
        self.max_length = Max_length
        self.table = [None] * Max_length

    def hash_fun(self,key):
        return hash(key) % self.max_length    

    def insert(self,key,value):
        index = self.hash_fun(key)
    
        if self.table[index] is None:
            self.table[index] = [(key,value)]
            self.size += 1
        else:
            for i,(existing_key,value) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = value
                    return
            self.table[index].append((key,value))    
            self.size += 1

    def search(self,key):
        index = self.hash_fun(key)

        if self.table[index]:
            for (existing_key,value) in self.table:
                if existing_key == key:
                    return value
        return None    

    def remove(self,key):
        index = self.hash_fun(key)

        if self.table[index]:
            for i ,(existing_key,value) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    return 
                
    def length(self):
        return self.length
    
    def display(self):
        for table in self.table:
            if table:
                for (i,j) in table:
                    print(i,j)



        