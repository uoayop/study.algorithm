#k번째 수
#힙
#https://www.acmicpc.net/problem/11004

import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().rsplit())

nums = list(map(int,input().rsplit()))
heapq.heapify(nums)

for _ in range(k-1):
    heapq.heappop(nums)

print(heapq.heappop(nums))