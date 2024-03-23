def heap_sort(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
    return print(arr)   


def heapify(arr,n,index):
    right = 2*index + 1
    left = 2*index + 2

    largest = index

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if index != largest:
        arr[index],arr[largest] = arr[largest],arr[index]
        heapify(arr,n,largest)        



array = [3,5,6,8,93,2,66,9]

heap_sort(array)        