array = [30,6,9,2,15,3,1,6,9]

def Insertionsort(list):
    n = len(list)
    for i in range(1,n):
        current_value = list[i]
        j = i-1
        while j >= 0 and list[j] > current_value:
            list[j+1] = list[j]
            j -= 1
        list[j+1]  = current_value

    return list    

print(Insertionsort(array))        


