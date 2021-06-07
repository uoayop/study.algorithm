# ATM
# 그리디
# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

n = int(input())
humans = sorted(list(map(int,input().rsplit())))

dp = [0 for _ in range(n)]
dp[0] = humans[0]

for i in range(1,n):
    dp[i] += dp[i-1] + humans[i]

print(sum(dp))
