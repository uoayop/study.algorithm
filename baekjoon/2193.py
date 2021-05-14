# 이친수
# https://www.acmicpc.net/problem/2193

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

if n < 3:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1

    # n-1 이친수에 0 을 추가한 경우 +  n-2 이친수에 01을 추가한 경우
    for i in range(3,n+1):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp[n])