array = [30,6,9,2,15,3,1,6,9]

def Bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr     

print(Bubblesort(array))       