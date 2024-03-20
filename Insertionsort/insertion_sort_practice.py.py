array = [30,6,9,2,15,3,1,6,9]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        current_value = arr[i]

        while j >= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current_value  

    return arr      

print(insertion_sort(array))
