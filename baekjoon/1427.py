# 소트인사이드
# https://www.acmicpc.net/problem/1427

import sys
import heapq
input = sys.stdin.readline

# n = int(input())
# q = []

# for c in str(n):
#     heapq.heappush(q, int(c) * -1)

# for _ in range(len(q)):
#     print(heapq.heappop(q) * -1,end="")

n = sorted(list(input().rstrip()),reverse = True)
print(''.join(n))
