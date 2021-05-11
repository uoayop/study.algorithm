# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x, y = map(int,input().rsplit())
    heapq.heappush(q,(x,y))

for _ in range(len(q)):
    x, y = heapq.heappop(q)
    print(x,y)

