#포도주 시식
#https://www.acmicpc.net/problem/2156
#DP

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input().rstrip())
wines = [0] * (n+1)
dist = [0] * (n+1)

for i in range(1,n+1):
    wines[i] = int(input().rstrip())

if n==1:
    print(wines[1])
    sys.exit(0)
elif n==2:
    print(wines[1]+wines[2])
    sys.exit(0)
else:
    dist[1] = wines[1]
    dist[2] = wines[1] + wines[2]
    dist[3] = max(wines[1] + wines[3], wines[2] + wines[3], dist[2])

    for i in range(4,n+1):
        # dist[i] = wines[i] + max(wines[i-1] + dist[i-3], 
        #                         wines[i-2] + dist[i-3])
        dist[i] = max(wines[i] + wines[i-1] + dist[i-3], 
                      wines[i] + dist[i-2],
                      dist[i-1])

    print(dist[n])