# def factorial(n):
#     if n <= 1:
#         return n
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))    






####### find the sum of elements in a list using recursion


# def sum_of_element_list(list):
#     if not list:
#         return 0
#     else:
#         return list[0] + sum_of_element_list(list[1:])
    

# list = [1,2,3,5,6,7,89]
    
# print(sum(list))  
# print(sum_of_element_list(list))





# def sum(n):               
#     if n <= 1:
#         return n   
#     else:
#         return n + sum(n-1)
    
# print(sum(5))    



# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(4))    
    



# def fibonacci(value,a=0,b=1):
#     if value >= 0:
#         print(a,end=' ')
#         return fibonacci(value-1,b,a+b)
#     else:
#         return
# fibonacci(5)    











# count = 0
# max_count = 0
# sub_string = ''
# max_string = ''
# first = s[0]


# def binarysearch(array,target,low,high):
#     if low < high:
#         print('a')
#         mid = (low+high)//2
#         mid_element = array[mid]
#         print(mid_element)
#         if mid_element == target:
#             return f"target element index is {mid}"
#         elif mid_element > target:
#             return binarysearch(array,target,low,mid)
#         elif mid_element < target:
#             return binarysearch(array,target,mid,high)
#     else:
#         return f"target element is not in this list"



# list = [2,4,7,9,10,14,34] 
# print(binarysearch(list,14,0,len(list)))   







# def is_palindrome(string):
#     if len(string) <= 1:
#         print("The string is palindrome")
#     elif string[0] == string[-1]:
#         is_palindrome(string[1:-1])  
#     else:
#         print("string is not palindrom")      

# s= 'malayalam'
# is_palindrome(s)


def flattened_list(nested_list):
    flat_list = []

    for i in nested_list:
        if isinstance(i,list ):
            flat_list.extend(flattened_list(i))
        else:
            flat_list.append(i)
    return flat_list
 

nested_list = [1, [2, 3, [4, 5]], 6, [7, 8, [9, 10]]]
print(flattened_list(nested_list))



# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
    
# string = 'favas'
# print(reverse(string)) 