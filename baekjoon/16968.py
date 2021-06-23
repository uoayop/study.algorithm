# 차량번호판
# 브르투포스
# https://www.acmicpc.net/problem/16968

import sys
input = sys.stdin.readline

nums = list(input().rstrip())
c, d = 26, 10

pre = nums[0]
answer = 26 if pre == 'c' else 10

for i in range(1, len(nums)):
    if nums[i] == pre:
        if pre == 'c':
            c  = 25
            answer *= c
        else:
            d = 9
            answer *= d
    else:
        if pre == 'c':
            c = 26
            answer *= d
        else:
            d = 10
            answer *= c
    pre = nums[i]

print(answer)
