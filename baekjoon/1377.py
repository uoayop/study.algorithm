# 버블소트
# https://www.acmicpc.net/problem/1377

# 1838번이랑 동일한 문제

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

before = defaultdict(int)
for i,num in enumerate(a):
    before[num]=i

a.sort()

after = defaultdict(int)
for i,num in enumerate(a):
    after[num] = i

answer = 0
for num in before:
    minus = before[num] - after[num]
    if (minus > 0 and minus > answer):
        answer = minus

print(answer+1)