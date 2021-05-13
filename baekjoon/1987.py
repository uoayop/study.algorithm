# 알파벳
# https://www.acmicpc.net/problem/1987
# bfs

import sys
input = sys.stdin.readline

R, C = map(int,input().rsplit())
maps = [[] for _ in range(R)]

for i in range(R):
    maps[i] = list(input().rstrip())

x, y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

alpha, q = [], set()
q.add((x,y,1,maps[0][0]))
answer = 0

while q:
    x,y,count,alpha = q.pop()
    answer = max(answer, count)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if (maps[nx][ny] not in alpha):
                q.add((nx,ny,count+1,alpha + maps[nx][ny]))

print(answer)