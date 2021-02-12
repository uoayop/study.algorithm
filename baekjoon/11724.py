#연결 요소의 개수
#dfs
#https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int,input().rstrip().rsplit())
graph, visited = [[] for _ in range(n+1)], [False] * (n+1)
cnt = 0

for _ in range(m):
    u,v = map(int,input().rstrip().rsplit())
    graph[u].append(v)
    graph[v].append(u)
    # if u not in graph:
    #     graph[u] = [v]
    # else:
    #     graph[u].append(v)

    # if v not in graph:
    #     graph[v] = [u]
    # else:
    #     graph[v].append(u)


def dfs(u):
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

    # if u in graph:
    #     while graph[u]:
    #         v = graph[u].pop()
    #         if visited[v] == 0:
    #             dfs(graph,v)
    #             return 1
    #         else:
    #             return 0

    # visited[u] = 0
    # if u not in graph and visited[u]==0:        
    #     return 1

for i in range(1,len(graph)):
    if not visited[i]:
        dfs(i)
        cnt += 1 

print(cnt)