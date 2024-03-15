array = [30,6,9,2,15,3,1,6,9]

def Quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]

        return Quick_sort(less_than_pivot) + [pivot] + Quick_sort(greater_than_pivot)
    

print(Quick_sort(array))