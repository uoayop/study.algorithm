#트리의 부모 찾기
#dfs
#https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input().rstrip())
graph = {}
answer = [0] * (n+1)
visited = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().rstrip().rsplit())
    if x not in graph:
        graph[x]=[y]
    else:
        graph[x].append(y)

    if y not in graph:
        graph[y]=[x]
    else:
        graph[y].append(x)

def dfs(v,answer):
    visited[v] = 1
    for u in graph[v]:
        if visited[u]==0:
            if u!=1:
                dfs(u,answer)
                answer[u] = v
        else:
            if u!=1:
                answer[u] = v

    return answer
        
answer = (dfs(1,answer))[2:]
for num in answer:
    print(num)