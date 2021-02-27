#특정한 최단 경로
#https://www.acmicpc.net/problem/1504
#다익스트라

import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize

n,e = map(int,input().rstrip().rsplit())
graph = [[ 0 for _ in range(n+1) ] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int,input().rstrip().rsplit())
    if graph[a][b]==0 or graph[a][b] > c:
        graph[a][b] = c
        graph[b][a] = c

v1, v2 = map(int,input().rstrip().rsplit())

path1 = [1, v1, v2, n]
path2 = [1, v2, v1, n]

answer1 = 0
answer2 = 0
answer = 0

for i in range(0,3):
    now_n = path1[i]
    next_n = path1[i+1]

    if graph[now_n][next_n]==0:
        answer1 = -1
        break
    answer1 += graph[now_n][next_n]

for i in range(0,3):
    now_n = path2[i]
    next_n = path2[i+1]

    if graph[now_n][next_n]==0:
        answer2 = -1
        break
    answer2 += graph[now_n][next_n]
    
if answer1 == -1 and answer2 == -1:
    print(-1)
elif answer == -1 and answer2!= -1:
    print(answer2)
elif answer != -1 and answer2== -1:
    print(answer1)
elif answer != -1 and answer2 != -1:
    print(min(answer1,answer2))
