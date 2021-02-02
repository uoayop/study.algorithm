#10773 제로
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
sum = 0

for i in range(temp):
    order = int(sys.stdin.readline().rstrip())

    if (order==0):
        stack.pop()
    else:
        stack.push(order)
    
for i in range(stack.size()):
    sum += stack.pop()

print(sum)