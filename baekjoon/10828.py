#10828 스택

import sys

class stack:
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
    def size(self):
        return self.pos
    def empty(self):
        if self.pos==0 : return 1
        return 0
    def top(self):
        if self.pos==0: return -1
        return self.stack[self.pos-1]

temp = int(sys.stdin.readline().rstrip())
stack=stack()

for i in range(temp):
    order = sys.stdin.readline().rstrip().split()

    cm = order[0]

    if cm=='push':
        stack.push(order[1])
    elif cm=='pop':
        print(stack.pop())
    elif cm=='size':
        print(stack.size())
    elif cm=='empty':
        print(stack.empty())
    elif cm=='top':
        print(stack.top())