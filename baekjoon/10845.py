#10845 큐

import sys
import collections

deq = collections.deque()

temp = int(sys.stdin.readline().rstrip())

for i in range(temp):
    order = sys.stdin.readline().rstrip().split()

    lendeq = len(deq)
    cm = order[0]

    if cm=='push':
        deq.append(order[1])
    elif cm=='pop':
        if (len(deq) != 0 ):
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


# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def push(self,a):
#         self.queue.append(a)
#     def pop(self):
#         if self.empty():
#             return -1
#         else:
#             return self.queue.pop(0)
#     def size(self):
#         return len(self.queue)
#     def empty(self):
#         if (not self.queue == True):
#             return 1
#         else: return 0
#     def front(self):
#         if self.empty(): 
#             return -1
#         else:
#             return self.queue[0]
#     def back(self):
#         if self.empty(): 
#             return -1
#         else:
#             return self.queue[-1]