array = [30,6,9,2,15,3,1,6,9]

def Merge_sort(arr):
    if len(arr) > 1:
        
        mid = len(arr)//2

        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        Merge_sort(left_arr)
        Merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1

            k += 1

        if i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        if j < len(right_arr):
            arr[k] = right_arr[j]   
            j += 1
            k += 1


    return arr   

print(Merge_sort(array)) 

