# 가장 긴 증가하는 부분 순열
# https://www.acmicpc.net/problem/11053
# dp

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().rsplit()))
dp = [1] * n

# dp[i] = 수열의 i번째 요소까지 만들 수 있는 가장 긴 배열의 길이

# i = 0, j=0 / i = 1, j=0,1 / i=2, j=0,1,2 ...
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(dp)