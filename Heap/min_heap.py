class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def build_heap(self,arr):
        self.heap = arr[:] 
        n = len(self.heap)

        for i in range(n//2,-1,-1):
            self.heap_down(i)

    
    def insert(self,value):
        self.heap.append(value)
        self.heap_up(len(self.heap)-1)

    def heap_up(self,index):
        parent = (index-1)//2

        while index > 0 and self.heap[parent] > self.heap[index]:
            self.swap(parent,index)
            index = parent
            parent = (index-1)//2

    def heap_down(self,index):
        left_child = (2*index) + 1
        right_child = (2*index) + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest =left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        if smallest != index:
            self.swap(index,smallest)
            self.heap_down(smallest)    


    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]    

    def remove(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        self.swap(0,len(self.heap)-1)
        self.heap.pop()
        self.heap_down(0)
        return
    
    # def remove_value(self,value):
    #     if value not in self.heap:
    #         return False    
    #     index = self.heap.index(value)
    #     self.heap[index] = float('-inf')

    #     self.heap_up(index)
    #     self.heap[0] = self.heap.pop()
    #     self.heap_down(0)
        


min_heap = MinHeap()

min_heap.build_heap([3,5,6,8,93,2,66,9])
min_heap.remove()

min_heap.remove_value(9)


min_heap.insert(10)
print(min_heap.heap)
