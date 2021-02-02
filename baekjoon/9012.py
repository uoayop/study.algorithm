#9012 괄호

import sys

class Stack:
    def __init__(self):
        self.stack=[]
        self.pos=0
    def push(self,a):
        self.stack.append(a)
        self.pos+=1
    def pop(self):
        if self.pos == 0 : return -1
        self.pos-=1
        return self.stack.pop()

n=int(sys.stdin.readline().rstrip())

for i in range(0,n):
    stack=Stack()
    left=0
    str = sys.stdin.readline().rstrip()
    length = len(str)

    for j in range(0,length):

        if (str[j]=='('):
            stack.push('(')
            left+=1
        if (str[j]==')'):
            stack.pop()
            left-=1

    if (str[0] == ')' or str[-1] == '(' or stack.pos != 0 or left<0):
        print("NO")

    else:
        print("YES")



# import sys

# def judge(str,len):
#     left=0
#     right=0

#     for i in range(len):
#         if (str[i]=='('):
#             left+=1
#         elif (str[i]==')'):
#             right+=1
#         if (left<right): break
    
#     if (left == right and str[0]!=')'): print("YES")
#     else : print("NO")

# n=int(sys.stdin.readline().rstrip())

# for i in range(0,n):
#     str = sys.stdin.readline().rstrip()
#     length = len(str)

#     judge(str,length)

