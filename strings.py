
# s = "aabcdaabbbbbbbbbbacaaaaaabbaaaaaaaaaaaacaaadgdaaalmmaa"

# a_count = 0
# count = 0
# for i in range(len(s)):

#     if s[i]=='a':
#         count +=1
#     if s[i] != 'a':
#         if count == 2:
#             a_count += 1
#         count = 0  
#     if count == 2 and i == len(s)-1:
#         a_count += 1    
# print(a_count)    



# s = "aabcdaaabbbbbbbbbbbbbbbacaaaaaabbaaaaaaaaaaaacaaadgdaaalmaaaaaa"

# count = 0
# max_count = 0
# sub_string = ''
# max_string = ''
# count = 0
# first = s[0]


# for i in range(len(s)):
    
#     if  s[i] == first:
#         sub_string += s[i]
#         count += 1

#     elif s[i] != first:
#         if count > max_count:
#             max_count = count 
#             max_string = sub_string
#         count = 1
#         first = s[i]
#         sub_string = s[i]
   
   
# print(max_string)   


# s = 'favas'
# str = ''
# for i in s:
#     str = i + str
# print(str)


#removing unwanted space in strings


# def removeUnwantedSpace(string):
#     prev = ''
#     new = ''
#     for char in string:
#         if char == ' ' and  prev == ' ':
#             continue
#         new += char
#         prev = char
#     print(new)    



# string = 'Hello           how                are             you'
# removeUnwantedSpace(string)    



'''capitalize strings in different method '''

# s = "hi hello world"
# capitalized_s = s.capitalize()
# print(capitalized_s)  # Output: "Hi hello world"




# s = "hi hello world"
# title_s = s.title()
# print(title_s)  # Output: "Hi Hello World"




# s = "hi hello world"
# upper_s = s.upper()
# print(upper_s)  # Output: "HI HELLO WORLD"



# s = "hi hello world"
# capitalized_s = ' '.join(word.capitalize() for word in s.split())
# print(capitalized_s)  # Output: "Hi Hello World"




# s = "hi hello world"

# new_s = ''
# flag = True

# for i in s:
#     if flag and i.isalpha():
#         new_s += i.upper()
#         flag = False
#     else:
#         new_s += i

#     if i == ' ':
#         flag = True

# print(new_s)
