#계단 오르기
#DP
#https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline

n = int(input().rstrip())
stairs=[]
dp = [0] * (n+1)

for _ in range(n):
    temp = int(input().rstrip())
    stairs.append(temp)


dp[0]=stairs[0]
if n==1:
    print(dp[0])
    sys.exit(0)

dp[1]=stairs[1]+stairs[0]
if n==2:
    print(dp[1])
    sys.exit(0)

dp[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3,n):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[n-1])