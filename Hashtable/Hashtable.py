class Hashtable:
    def __init__(self,size=6) -> None:
        self.size = size
        self.length = 0
        self.table = [None] * size

    def hash_fun(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        index = self.hash_fun(key)

        if self.table[index] is None:
            self.table[index] = [(key,value)]   
            self.length += 1
        else:
            for i , (existing_key,_) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = value
                    return
                
            self.table[index].append((key,value))
            self.length += 1

    def search(self,key):     
        index = self.hash_fun(key)

        if self.table[index]:
            for i, (existing_key,value) in enumerate(self.table[index]):
                if existing_key == key:
                    return value
        return None    

    def remove(self,key):
        index = self.hash_fun(key)

        if self.table[index]:
            for i, (existing_key,value) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    return 

    def display(self):
        for bucket in self.table:
            if bucket:
                for i,j in bucket:
                    print(i,j)
                   




hashtable = Hashtable()

hashtable.insert('favas',1)
hashtable.insert('saban',2)
hashtable.insert('fayis',3)
hashtable.insert('siyaf',4)
hashtable.insert('jabbar',6)
hashtable.insert('salman',7)
hashtable.insert('sulaiman',8)


hashtable.display()

                
              

