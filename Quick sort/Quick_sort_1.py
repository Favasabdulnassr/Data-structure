def Quicksort(arr,left,right):
    if left < right:
        partition_index = partition(arr,left,right)
        Quicksort(arr,partition_index + 1,right)
        Quicksort(arr,left,partition_index-1)

    return arr    



def partition(arr,left,right):
    i = left + 1
    j = right
    pivot = arr[left]

    while i < j:

        while i < right and arr[i] <= pivot:
            i += 1

        while j > left and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i],arr[j] = arr[j],arr[i]

    if arr[j] < pivot:
        arr[j],arr[left] = arr[left],arr[j]   

    return j      

array = [30,6,9,2,15,3,1,6,9]

print(Quicksort(array,0,len(array)-1))




