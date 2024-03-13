s = "hi hello world"

stack = []
new = ''

for i in s:
    if i != ' ':
        stack.append(i)
    if i == ' ' or i == s[-1]:
        while stack:
            new += stack[-1]
            stack.pop()
        new += ' ' 
print(new)           