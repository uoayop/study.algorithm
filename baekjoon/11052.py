#카드 구매하기
# https://www.acmicpc.net/problem/11052
# dp

import sys
input = sys.stdin.readline

n = int(input())
p = ['dummy'] + list(map(int,input().rsplit()))

# dp[i] = 카드 i개를 구매할 때 가질 수 있는 금액의 최댓값
dp = [0] * (n+1)
dp[1] = p[1]
dp[2] = max(dp[1]*2, p[2])

for i in range(3,n+1):
    for j in range(1,i+1):
        dp[i] = max(p[i], dp[i], dp[j] + dp[i-j])

print(dp[n])