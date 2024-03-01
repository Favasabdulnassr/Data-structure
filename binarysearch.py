def linearsearch(target,array):
    for item in range(len(array)):
        if array[item] == target:
            return f"target element found at index {item}"
    return f"target element is not found"

array = [3,4,1,7,996,5]

print(linearsearch(996,array))


def binarysearch(target,array):
    low,high = 0 , len(array)

    while low < high:
        mid = (low + high)//2
        mid_element = array[mid]
        print(mid_element)

        if mid_element == target:
            return f"target found at index {mid}"
        elif mid_element < target:
             low = mid 
        else:
            high = mid 
    return f"target element is not in this array"   



# array = [1,3,4,5,9,79]
# print(binarysearch(4,array))
