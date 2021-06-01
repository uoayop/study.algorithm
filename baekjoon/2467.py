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

# for l in range(n):
#     curr = liquids[l]
#     r = l + 1
#     while r < n:
#         curr += liquids[r]
    
#         if abs(answer) > abs(curr):
#             answer = curr
#             ansl, ansr = liquids[l], liquids[r]

#         curr -= liquids[r]
#         r += 1
#         print("[l]:{2}, [r]:{3}, [answer]:{0}, [abs(curr)]:{1}".format(answer, abs(curr),l,r))
    
#     curr -= liquids[l]

print(ansl, ansr)
