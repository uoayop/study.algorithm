# 좌표 압축
# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().rsplit()))
sortednums = {}

for i,n in enumerate(sorted(list(set(nums)))):
    sortednums[n] = i

for n in nums:
    print(sortednums[n],end=" ")
print()