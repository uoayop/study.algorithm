#벽 부수고 이동하기
#bfs
#https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input=sys.stdin.readline

n, m = map(int,input().rstrip().rsplit())
queue = deque()

matrix = []
visited = [[[0]*(m+1) for _ in range(n+1)] for _ in range(2) ]
# [3차원 배열을 사용한 이유]
# visited[x][y][벽을 뚫었는지 체크해주는 변수 : check] 다음과 같이 3차원 배열을 해주었다.
# 벽을 뚫고 갔을 때와 벽을 뚫고 가지 않았을 때 비교해줘야 한다.
#5 4
#0001
#1101
#0001
#0111
#0010
#이 예시를 보면 처음에 아래에 있는 벽을 뚫고 가는 것이 처음엔 최적해지만 나중에 도착지에 가서 벽을 하나 더 뚫어야 함을 고려할 수 없다.
#따라서 벽을 뚫었을때와 벽을 뚫지 않았을 때를 방문을 분리해서 체크를 해야한다.


dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    row = input().rstrip()
    matrix.append(row)

def bfs():
    queue.append([0,0,1,0])

    while queue:
        x,y,cnt,check = queue.popleft()

        if x == n-1 and y == m-1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 방문했으면 continue
                if visited[check][nx][ny] == 1:
                    continue
                #방문 안했으면
                else:
                    visited[check][nx][ny] = 1

                    #벽이면
                    if matrix[nx][ny] == '1':
                        #벽 부신적이 없으면, 부시고 방문해줘
                        if check == 0 :
                            queue.append([nx,ny,cnt+1,1])
                    #길이면
                    else:
                        queue.append([nx,ny,cnt+1,check])

    return -1

print(bfs())