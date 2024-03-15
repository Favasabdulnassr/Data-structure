def Quicksort(arr,left,right):
    if left < right:
        partition_index = Partition(arr,left,right)

        Quicksort(arr,left,partition_index-1)
        Quicksort(arr,partition_index+1,right)
    return arr    



def Partition(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] <= pivot:
            i += 1

        while j > left and arr[j] > pivot:
            j -= 1
                  
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]

    if arr[i] > arr[right]:
        arr[i],arr[right] = arr[right],arr[i]

    return i    




array = [30,6,9,2,15,3,1,6,9]

print(Quicksort(array,0,len(array)-1))


