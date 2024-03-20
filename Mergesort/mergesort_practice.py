array = [30,6,9,2,15,3,1,6,9]

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])

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

        elif j < len(right_arr):
            arr[k]  = right_arr[j] 


    return arr  

print(merge_sort(array))                