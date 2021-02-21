#유기농 배추
#dfs
#https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    #배추밭 행 m, 배추밭 열 n, 배추 개수 k
    m,n,k = map(int,input().rsplit())
    graph = {}
    visited = [[0 for col in range(n)] for row in range(m)]
    count = 0
    ground = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for _ in range(k):
        x,y = map(int,input().rsplit())
        ground.append((x,y))
        
        graph[(x,y)]=[]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (nx,ny) in graph:
                graph[(nx,ny)].append((x,y))
                graph[(x,y)].append((nx,ny))

    def dfs(i,j):
        if visited[i][j]==0:
            visited[i][j]=1
            
            while graph[(i,j)]:
                temp = (graph[(i,j)].pop(0))
                dfs(temp[0],temp[1])
            return 1
        else:
            return 0

    for baechoo in ground:
        count += dfs(baechoo[0],baechoo[1])
        
    print(count)
