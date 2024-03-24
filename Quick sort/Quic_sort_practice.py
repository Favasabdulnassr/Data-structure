array = [30,6,9,2,15,3,1,6,9]

def Quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [i for i in arr[1:] if i <= pivot]
        greater_than_pivot = [i for i in arr[1:] if i > pivot]

        return Quicksort(less_than_pivot) + [pivot] + Quicksort(greater_than_pivot)
    

print(Quicksort(array))
                                                                                              



                                                                                              