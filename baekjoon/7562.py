#나이트의 이동
#dfs, bfs
#https://www.acmicpc.net/problem/7562

import sys
from collections import deque
input = sys.stdin.readline


T = int(input().rstrip())
for _ in range(T):
    l = int(input().rstrip())
    start_x, start_y = map(int,input().rsplit())
    end_x, end_y = map(int,input().rsplit())
    visited = [[0]*l for _ in range(l)]
    visited[start_x][start_y] = 1

    dx = [-2, -2, 2, 2, -1, 1,-1, 1]
    dy = [-1, 1,-1, 1, -2, -2, 2, 2]

    queue = deque()
    queue.append((start_x,start_y,0))

    while (queue):
        #print(queue)
        temp = queue.popleft()
        x, y = temp[0],temp[1]

        if x == end_x and y == end_y:
            print(temp[2])
            break
        
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny]==0:
                visited[nx][ny] = 1
                queue.append((nx,ny,temp[2]+1))
