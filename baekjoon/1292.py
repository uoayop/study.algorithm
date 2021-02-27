#쉽게 푸는 문제
#https://www.acmicpc.net/problem/1292

import sys
input = sys.stdin.readline

start,end = map(int,input().rstrip().rsplit())
nums = [0]
answer = 0

for i in range(1,end+1):
    for j in range(i):
        nums.append(i)

for k in range(start,end+1):
    answer += nums[k]

print(answer)
