array = [30,6,9,2,15,3,1,6,9]

def Bubblesort1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

print(Bubblesort1(array))            