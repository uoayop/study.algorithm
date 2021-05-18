# 2xn 타일링2
# https://www.acmicpc.net/problem/11727
# dp

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 3

if n < 3:
    print(dp[n])
else:
    for i in range(3, n+1):
        # 2 x i 크기의 직사각형을 채우는 방법 가짓수 = dp[0]
        # dp[i] = dp[i-1] + (2x1 1개) / dp[i-2] + (2x2 1개/ 1x2 2개)
        dp[i] = (dp[i-1] + (dp[i-2] * 2) % 10007) % 10007

    print(dp[n])
