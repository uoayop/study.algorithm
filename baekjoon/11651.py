# 좌표 정렬하기2
# https://www.acmicpc.net/problem/11651

import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

# for _ in range(n):
#     x, y = map(int,input().rsplit())
#     heapq.heappush(q, (y,x))

# for _ in range(len(q)):
#     y, x = heapq.heappop(q)
#     print(x, y)

for _ in range(n):
    q.append(list(map(int, input().rsplit())))

q = sorted(q, key=lambda x: (x[1], x[0]))

for n1,n2 in q:
    print(n1,n2)
