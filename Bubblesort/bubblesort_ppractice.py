array = [30,6,9,2,15,3,1,6,9]

def Bubble_sort(arr):
    n = len(arr)-1

    while n > 0:
        i = 0
        
        while i < n:
            j = i + 1
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            i = j
        n -= 1

    return arr

print(Bubble_sort(array))    
