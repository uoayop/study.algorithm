#18258 큐 2

import sys
import collections

deq = collections.deque()

temp = int(sys.stdin.readline().rstrip())

for i in range(temp):
    order = sys.stdin.readline().rstrip().split()

    cm = order[0]

    if cm=='push':
        deq.append(order[1])
    elif cm=='pop':
        if (len(deq)!=0):
            print(deq.popleft())
        else: print(-1)
    elif cm=='size':
        print(len(deq))
    elif cm=='empty':
        if (len(deq)==0): print(1)
        else: print(0)
    elif cm=='front':
        if (len(deq)!=0): print(deq[0])
        else: print(-1)
    elif cm=='back':
        if (len(deq)!=0): print(deq[-1])
        else: print(-1)



# class queue:
#     def __init__(self):
#         self.queue=[]
#         self.back=0
#         self.front=0
#     def push(self,a):
#         self.queue.insert(0,a)
#         self.back+=1
#     def pop(self):
#         if self.back == 0 : return -1
#         self.back-=1
#         return self.queue.pop()
#     def size(self):
#         return self.back
#     def empty(self):
#         if self.back==0 : return 1
#         return 0
#     def getback(self):
#         if self.back==0: return -1
#         return self.queue[0]
#     def getfront(self):
#         if self.back==0: return -1
#         return self.queue[self.back-1]
