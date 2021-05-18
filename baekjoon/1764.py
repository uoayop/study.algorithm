# 듣보잡
# https://www.acmicpc.net/problem/1764
# 정렬

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int,input().rsplit())
arr = defaultdict(int)
for _ in range(n):
    arr[input().rstrip()] += 1

for _ in range(m):
    arr[input().rstrip()] -= 1

result = []
for human,v in arr.items():
    if v == 0:
        result.append(human)

print(len(result))
for human in sorted(result):
    print(human)