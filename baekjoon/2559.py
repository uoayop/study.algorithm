# 수열
# 투포인터
# https://www.acmicpc.net/problem/2559

import sys
input = sys.stdin.readline

n, k = map(int, input().rsplit())
nums = list(map(int, input().rsplit()))

r, answer, curr = 0, float('-inf'), 0

for l in range(n-k+1):
    while r < l + k and r < n:
        curr += nums[r]
        r += 1
    print("[curr]:{0}, [r]:{1}, [answer]:{2}".format(curr, r, answer))

    answer = max(answer, curr)
    curr -= nums[l]

print(answer)
