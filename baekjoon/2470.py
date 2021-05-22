# 두 용액
# https://www.acmicpc.net/problem/2470
# 이분탐색

import sys
input = sys.stdin.readline

# 0에 가까운 두 용액 찾기
n = int(input())
sol = sorted(list(map(int,input().rsplit())))

l, r = 0, n-1
lowest = sys.maxsize
low_l, low_r = 0, 0

while l < r:
    if abs(sol[l] + sol[r]) < lowest:
        lowest = abs(sol[l] + sol[r])
        low_l, low_r = sol[l], sol[r]
    else:
        if abs(sol[l]) < abs(sol[r]):
            r -= 1
        else:
            l += 1

print(low_l, low_r)
