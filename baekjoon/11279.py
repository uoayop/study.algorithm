#최대힙
#https://www.acmicpc.net/problem/11279

import sys
import heapq

heap = []
tc=int(sys.stdin.readline().rstrip())
for i in range(tc):
    order = int(sys.stdin.readline().rstrip())
    if order==0:
        if len(heap)==0:
            print(0)
        else:
            print(-(heapq.heappop(heap)))
    else:
        heapq.heappush(heap,-order)
        

