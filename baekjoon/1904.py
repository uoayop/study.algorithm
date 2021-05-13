# 01타일
#dp
# https://www.acmicpc.net/problem/1904

# d(n) = 크기가 n일때 모든 가짓수
# d(n-1) = d(n-2) + [1]
# d(n-2) = d(n-3) + [11,00]

# d(1) = 1
# d(2) = 2
# d(3) = d(2) + 1
# d(4) = d(3) + 1

import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = ((dp[i-1] % 15746) + (dp[i-2] % 15746)) % 15746

print(dp[n])