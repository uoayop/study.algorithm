# 배열 합치기
# 투 포인터
# https://www.acmicpc.net/problem/11728

import sys
input = sys.stdin.readline

n, m = map(int, input().rsplit())

a = list(map(int, input().rsplit()))
b = list(map(int, input().rsplit()))

l, r = 0, 0
result = []
while l < n and r < m:
    if a[l] < b[r]:
        result.append(a[l])
        l += 1
    else:
        result.append(b[r])
        r += 1
    
    print(result, l, r)

while l < n:
    result.append(a[l])
    l += 1

while r < m:
    result.append(b[r])
    r += 1

print(" ".join(map(str, result)))
