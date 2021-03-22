#리그 오브 레전설
#dp
#https://www.acmicpc.net/problem/17271

import sys
input = sys.stdin.readline

n, m = map(int,input().rsplit())

dp = [1] * (n+1)

# index error가 나지 않도록 해준다.
if n >= m:
    dp[m] = 2

for i in range(m+1, n+1):
    dp[i] = (dp[i-1] + dp[i-m]) % 1000000007

print(dp[n] % 1000000007)