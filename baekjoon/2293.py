# 동전 1
# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

n, k = map(int, input().rsplit())
coins = []

for _ in range(n):
    coins.append(int(input()))

# dp[i] = i원 동전을 이용해서 j원을 만들 수 있는 방법의 수
dp = [0] * (k+1)
dp[0] = 1

for i in range(n):
    for j in range(coins[i], k+1):
        if j >= coins[i]:
            dp[j] += dp[j-coins[i]]

print(dp[k])
