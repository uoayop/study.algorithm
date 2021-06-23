#괄호의 값
#시뮬레이션
#https://www.acmicpc.net/problem/2504

import sys
input = sys.stdin.readline

#() = 2, [] = 3, (x)= 2 * x, [x]= 3 * x, (xy) = x + y

# (()[[]])([])
# (2[3])(3)
# (2,9)(3)
# (11)(3)
# 22,6
# 28

stack = []
num = 1
s = input().rstrip()

def numCheck():
    if not stack:
        return False
    if type(stack[-1]) == int:
        return True
    else:
        return False

for c in s:
    if c=='(' or c=='[':
        stack.append(c)
    elif c==')':
        if not stack:
            print(0)
            break
        if stack[-1]=='(':
            stack.pop()
            stack.append(2)
            if len(stack) > 2 and type(stack[-2]) == int:
                stack.pop()
                stack.append(stack.pop() * 2)

        elif len(stack) > 2 and type(stack[-1]) == int and stack[-2] == '(':
            temp = stack[-1]
            stack.pop()
            stack.pop()
            stack.append(temp * 2)
        else:
            stack.append(c)

    elif c==']':
        if not stack:
            print(0)
            break
        if stack[-1]=='[':
            stack.pop()
            stack.append(3)
            if len(stack) > 2 and type(stack[-2]) == int:
                stack.pop()
                stack.append(stack.pop() * 3)

        elif len(stack) > 2 and type(stack[-1]) == int and stack[-2] == '[':
            temp = stack[-1]
            stack.pop()
            stack.pop()
            stack.append(temp * 3)
        else:
            stack.append(c)



    print(c, stack)

print(stack,end='')