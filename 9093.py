#9093 단어뒤집기

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

temp = int(sys.stdin.readline().rstrip())

for i in range(temp):
    stack = Stack()
    result = ""

    text = sys.stdin.readline().rstrip()

    for word in text:
        if word==' ':   #빈칸이면
            while (stack.pos!= 0): #스택이 빌때까지
                result+=stack.pop()
            result +=' '
        else:          #빈칸이 아니면
            stack.push(word)
    while (stack.pos!=0):
        result += stack.pop()
    print(result)



    # for j in range(len(string)):
    #     k=0
    #     for k in range(len(string[j])):
    #         stack.push((string[j])[k])
    # string=str(string)
    # for i in range(len(string)):
    #   print(stack.pop(),end="")




