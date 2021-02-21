#토마토
#dfs
#https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().rstrip().rsplit())
done_tomato = deque([])
matrix = [[0] * m for _ in range(n)]
day = 0

dx = [-1, 1, 0, 0]  #상, 하, 좌, 우
dy = [0, 0, -1, 1]

for i in range(n):
    row = input().rstrip().rsplit()
    for j,num in enumerate(row):
        matrix[i][j] = num

for row in range(n):
    for col in range(m):
        if matrix[row][col]=='1':
            done_tomato.append((row,col,0))

while done_tomato:
    row, col, cnt = done_tomato.popleft()
    for k in range(4):
        nx = row + dx[k]
        ny = col + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == '0':
                matrix[nx][ny] = '1'
                done_tomato.append((nx,ny,cnt+1))
                day = cnt + 1

def check(day):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0':
                return -1
    return day

print(check(day))
