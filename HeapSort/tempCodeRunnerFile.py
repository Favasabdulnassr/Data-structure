def heap_sort(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
    return arr
        



def heapify(arr,n,index):
    left_child = (2*index)-1
    right_child = (2*index)+1

    largest = index

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest =right_child

    if largest != index:
        arr[largest],arr[index] = arr[index],arr[largest]
        heapify(arr,n,largest)

        


array = [3,5,6,8,93,2,66,9]

print(heap_sort(array))