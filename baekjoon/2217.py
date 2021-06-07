# 로프
# 그리디
# https://www.acmicpc.net/problem/2217

import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    result.append(int(input()))

result.sort()
answer = 0

for i in result:
    answer = max(answer, i * n)
    n -= 1

print(answer)