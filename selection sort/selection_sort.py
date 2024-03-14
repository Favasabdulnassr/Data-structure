array = [30,6,9,2,15,3,1,6,9]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i

        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        
           
        arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(array))    