# #연결 요소의 개수
# #dfs
# #https://www.acmicpc.net/problem/11724

# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline

# n, m = map(int,input().rstrip().rsplit())
# #graph, visited = [[] for _ in range(n+1)], [False] * (n+1)
# graph, visited = {}, [False] * (n+1)
# cnt = 0

# for _ in range(m):
#     u,v = map(int,input().rstrip().rsplit())
#     # graph[u].append(v)
#     # graph[v].append(u)
#     if u not in graph:
#         graph[u] = [v]
#     else:
#         graph[u].append(v)

#     if v not in graph:
#         graph[v] = [u]
#     else:
#         graph[v].append(u)


# def dfs(u):
#     visited[u] = 1
#     # for v in graph[u]:
#     #     if not visited[v]:
#     #         dfs(v)

#     if u in graph:
#         for v in graph[u]:
#             if visited[v] == 0:
#                 dfs(v)

# for i in range(1,n+1):
#     if not visited[i]:
#         dfs(i)
#         cnt += 1 

# print(cnt)



#<----------기존의 내 코드로 다시 풀기------------>

#연결 요소의 개수
#dfs
#https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().rsplit())
graph, visited = {}, [0]*(n+1)
cnt = 0

for _ in range(m):
    u,v = map(int,input().rstrip().rsplit())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)

    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

def dfs(u):
    visited[u] = 1
    if u in graph:
        for v in graph[u]:
            if visited[v] == 0:
                dfs(v)

    return 1

for i in range(1,n+1):
    if visited[i] == 0:
        cnt += dfs(i)

print(cnt)