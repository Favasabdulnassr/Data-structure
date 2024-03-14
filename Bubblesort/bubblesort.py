array = [30,6,9,2,15,3,1,6,9]

def bubblesort(list):
    
    n = len(list) - 1
    while n > 0:
        i = 0
        while i < n:
            j = i+1
            if list[i] > list[j]:
                list[j],list[i] = list[i],list[j]
            i = j
        n -= 1
    return list    
print(bubblesort(array))              