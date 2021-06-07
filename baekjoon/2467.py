# 용액
# 투포인터
# https://www.acmicpc.net/problem/2467

import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().rsplit()))

l, r, curr, answer = 0, n-1, 0, sys.maxsize
ansl, ansr = 0, 0

while l < r:
    if abs(liquids[l] + liquids[r]) < answer:
        answer = abs(liquids[l] + liquids[r])
        ansl, ansr = liquids[l], liquids[r]
    
    if liquids[l] + liquids[r] < 0:
        l += 1
    else:
        r -= 1

print(ansl, ansr)
