# 앱
# https://www.acmicpc.net/problem/7579
# 배낭문제, dp

# https://claude-u.tistory.com/445
import sys
input = sys.stdin.readline

n, m = map(int, input().rsplit())
memories = list(map(int, input().rsplit()))
cost = list(map(int, input().rsplit()))

tc = sum(cost)
result = sys.maxsize

# dp[i][j] = 비용이 j일때, 처음 i개의 앱을 종료해 얻을 수 있는 최대 메모리
dp = [[0 for _ in range(tc+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(tc):
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], memories[i] + dp[i-1][j-cost[i]])

        if dp[i][j] >= m:
            result = min(result, j)

if m==0:
    print(0)
elif n==1:
    print(cost[0])
elif result == sys.maxsize:
    print(n*m)
else:
    print(result)
