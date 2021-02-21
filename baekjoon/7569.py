#토마토
#bfs
#https://www.acmicpc.net/problem/7569



import sys
#import numpy
from collections import deque

input = sys.stdin.readline

m,n,h = map(int,input().rstrip().rsplit())
queue = deque([])
#tomato = numpy.arange(m*n*h).reshape(h,n,m) #z x y
tomato = [[[0] * m for i in range(n)] for j in range(h)]
day = 0

dx = [-1, 1, 0, 0, 0, 0]  #상, 하, 좌, 우 , 위, 아래
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for hei in range(h):
    for row in range(n):
        temp = input().rstrip().rsplit()
        for col,num in enumerate(temp):
            tomato[hei][row][col] = num
            if num == '1':
                queue.append((hei,row,col,0))

while queue:
    #익은 토마토의 위치와 cnt를 꺼냄
    hei, row, col, cnt = queue.popleft()
    for k in range(6):
        nx = row + dx[k]
        ny = col + dy[k]
        nz = hei + dz[k]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            # 익은 토마토 상하좌우에 안익은 토마토가 있으면 익게 해주고, queue에 위치와 cnt+1을 넣어줌
            if tomato[nz][nx][ny] == '0':
                tomato[nz][nx][ny] = '1'
                queue.append((nz,nx,ny,cnt+1))
                day = cnt + 1

def check(day):
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == '0':
                    return -1
    return day

print(check(day))