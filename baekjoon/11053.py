# 가장 긴 증가하는 부분 순열
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().rsplit()))
dp = [1] * (n+1)
dp[1] = 1

# dp[i] = 수열의 i번째 요소까지의 최대 배열 길이

# i = 0, j=0 / i = 1, j=0,1 / i=2, j=0,1,2 ...
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(dp)