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

    for _ in range(k):
        x,y = map(int,input().rsplit())
        ground.append([x,y])

        if len(graph)==0:
            graph[(x,y)]=[]
        
        graph[(x,y)]=[]
        if (x-1, y) in graph:
            graph[(x-1, y)].append([x,y])
            graph[(x, y)].append([x-1,y])
        if (x+1, y) in graph:
            graph[(x+1, y)].append([x,y])
            graph[(x, y)].append([x+1,y])
        if (x, y-1) in graph:
            graph[(x, y-1)].append([x,y])
            graph[(x, y)].append([x,y-1])
        if (x, y+1) in graph:
            graph[(x, y+1)].append([x,y])
            graph[(x, y)].append([x,y+1])

    def dfs(i,j):
        if visited[i][j]==0:
            visited[i][j]=1
            #print("[return 1]",i,j,graph)
            while graph[(i,j)]:
                temp = (graph[(i,j)].pop(0))
                dfs(temp[0],temp[1])
            return 1
        else:
            #print("[return 0]",i,j,graph)
            return 0

    for baechoo in ground:
        count += dfs(baechoo[0],baechoo[1])
        
    print(count)
