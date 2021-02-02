#4949 균형잡힌 세상

while 1:
    string = list(input())
    if string == ['.']:
        break

    stack = []
    flag = True

    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack)==0 or stack[-1] == '[':
                flag = False
                break
            else:
                stack.pop()
        elif char == ']':
            if len(stack)==0 or stack[-1] == '(':
                flag = False
                break
            else:
                stack.pop()
    if len(stack)==0 and flag==True:
        print('yes')
    else:
        print('no')