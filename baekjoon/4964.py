#섬의 개수
#bfs
#https://www.acmicpc.net/problem/4963

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline


def dfs(node,cnt):
    x, y = node[0], node[1]
    
    if visited[x][y] == 0:
        visited[x][y] = 1
        while graph[node]:
            next_node = graph[node].pop()
            nx, ny = next_node[0], next_node[1]
            
            cnt += dfs((nx,ny),cnt)
        return 1
    else:
        return 0

while (1):
    w, h = map(int,input().rstrip().rsplit())

    if w==0 and h==0 : break

    island, graph = [], {}
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    # 하, 상, 좌, 우 , 상좌, 상우, 하좌, 하우
    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for _ in range(h):
        row = input().rstrip()
        row = row.replace(' ','')
        island.append(row)

    for i,row in enumerate(island):
        for j,check in enumerate(row):
            if check == '1':
                graph[(i,j)] = []
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < h and 0 <= ny < w:
                        if island[nx][ny] == '1':
                            graph[(i,j)].append((nx,ny))

    for node in graph:
        cnt += dfs(node,0)

    print(cnt)

