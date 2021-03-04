# #알고스팟
# #https://www.acmicpc.net/problem/1261
# #다익스트라

# import sys
# from collections import deque
# MAX_INT = 99999999
# input = sys.stdin.readline

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 가로 M, 세로 N
# m, n = map(int,input().rstrip().rsplit())
# min_cnt = MAX_INT
# matrix = []
# for _ in range(n):
#     row = input().rstrip()
#     matrix.append(row)

# visited = [[False for _ in range(m+1)] for _ in range(n+1)]
# visited[0][0] = True

# dist = [[MAX_INT for _ in range(m+1)] for _ in range(n+1)]
# dist[0][0] = 0

# q = deque()
# q.append(((0,0),0))
# while q:
#     p = q.popleft()
#     location, cnt = p[0], p[1]
#     cur_x, cur_y = location[0], location[1]

#     # print("[cur_x, cur_y, cnt, min_cnt]:",cur_x, cur_y,cnt,min_cnt)
#     # print("[q]:",q)
#     # if cur_x == n-1 and cur_y == m-1:
#     #     min_cnt = min(min_cnt,cnt)

#     for k in range(4):
#         nx = dx[k] + cur_x
#         ny = dy[k] + cur_y
#         if (0 <= nx < n and 0 <= ny < m):
#             # print("[{0},{1}]={2}".format(nx,ny,visited[nx][ny]))

#             #방문 했을 때
#             if visited[nx][ny]:
#                 # print("[방문 했지만 더 작을 때 {0},{1}]={2}".format(nx,ny,matrix[nx][ny]))
#                 if matrix[nx][ny] == '0':
#                     dist[nx][ny] = dist[cur_x][cur_y]
#                     q.append(((nx,ny),cnt))
#                 else:
#                     dist[nx][ny] = min(1 + dist[cur_x][cur_y], dist[nx][ny])
#                     q.append(((nx,ny),cnt+1))
                
#                 # if dist[nx][ny] > cnt + dist[cur_x][cur_y]:
#                 #     if matrix[nx][ny] == '0':
#                 #         dist[nx][ny] = dist[cur_x][cur_y]
#                 #         q.append(((nx,ny),cnt))
#                 #     else:
#                 #         dist[nx][ny] = cnt + dist[cur_x][cur_y]
#                 #         q.append(((nx,ny),cnt+1))

#             #방문 안했을때
#             else:
#                 visited[nx][ny] = True

#                 if matrix[nx][ny] == '0':
#                     # print("[방문 안했을 때 {0},{1}]={2}".format(nx,ny,matrix[nx][ny]))
#                     dist[nx][ny] = dist[cur_x][cur_y]
#                     q.append(((nx,ny),cnt))

#                 else:
#                     # print("[방문 했을 때 {0},{1}]={2}".format(nx,ny,matrix[nx][ny]))
#                     dist[nx][ny] = min(1 + dist[cur_x][cur_y], dist[nx][ny])
#                     q.append(((nx,ny),cnt+1))

# print(min(dist[n-1][m-2],dist[n-2][m-1]))

#알고스팟
#https://www.acmicpc.net/problem/1261
#다익스트라

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 가로 M, 세로 N
m, n = map(int,input().rstrip().rsplit())
matrix = []

for _ in range(n):
    row = input().rstrip()
    matrix.append(row)

dist = [[-1] *(m+1) for _ in range(n+1)]
dist[0][0]=0

q = deque()
q.append((0,0))


while q:
    p = q.popleft()
    cur_x, cur_y = p[0], p[1]

    for k in range(4):
        nx = dx[k] + cur_x
        ny = dy[k] + cur_y
        if (0 <= nx < n and 0 <= ny < m):
            #방문 했으면
            if dist[nx][ny]!=-1:
                continue

            # 벽이면 q의 오른쪽에 넣어줌
            if matrix[nx][ny] == '1':
                q.append((nx,ny))
                dist[nx][ny] = dist[cur_x][cur_y] + 1 
            else:
                # 길이면 q의 왼쪽에 넣어줌
                # => 더 빨리 탐색하기 위해서 왼쪽에 넣어줌
                q.appendleft((nx,ny))
                dist[nx][ny] = dist[cur_x][cur_y] 

print(dist[n-1][m-1])