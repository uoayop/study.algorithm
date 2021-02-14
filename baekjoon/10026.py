#적록색약
#bfs
#https://www.acmicpc.net/problem/10026


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    #현재 색상 좌표를 방문해준다.
    visited[x][y] = True
    current_color = matrix[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nx][ny]==False:
                if matrix[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j]==False:
            dfs(i,j)
            three_cnt += 1

#R을 G로 바꾸어준다. --> 적록색약은 같은 색으로 보기 때문에
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='R':
            matrix[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)



# import sys
# from collections import deque
# input = sys.stdin.readline


# #<------------아직 푸는중~~_--------------
# n = int(input().rstrip())
# matrix = []
# visited = [[[0] * n for _ in range(n)] for _ in range(2)]
# three_color_graph, three_cnt = {}, 0
# two_color_graph, two_cnt = {}, 0
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# for i in range(n):
#     row = input().rstrip()
#     matrix.append(row)

# for i,row in enumerate(matrix):
#     for j,check in enumerate(row):
#         for k in range(4):
#             nx = i + dx[k]
#             ny = j + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if (i,j) not in three_color_graph:
#                     three_color_graph[(i,j)]=[]
#                 if (i,j) not in two_color_graph:
#                     two_color_graph[(i,j)]=[]

#                 if check == 'R':
#                     if matrix[nx][ny] == 'R':
#                         #색맹 아닐때
#                         three_color_graph[(i,j)].append((nx,ny))
#                         two_color_graph[(i,j)].append((nx,ny))
#                     if matrix[nx][ny] == 'G':
#                         #색맹일때
#                         two_color_graph[(i,j)].append((nx,ny))
                            
#                 elif check == 'G':
#                     if matrix[nx][ny] == 'G':
#                         three_color_graph[(i,j)].append((nx,ny))
#                         two_color_graph[(i,j)].append((nx,ny))
#                     if matrix[nx][ny] == 'R':
#                         #색맹일때
#                         two_color_graph[(i,j)].append((nx,ny))
                
#                 elif check == 'B':
#                     if matrix[nx][ny] == 'B':
#                         three_color_graph[(i,j)].append((nx,ny))
#                         two_color_graph[(i,j)].append((nx,ny))
# # print(two_color_graph)
# # print(three_color_graph)
# def two_bfs(i,j):
#     queue = deque()
#     queue.append((i,j))

#     while queue:
#         x, y = queue.popleft()
#         visited[1][x][y] = 1
#         for v1,v2 in two_color_graph[(x,y)]:
#             if visited[1][v1][v2] == 0:
#                 visited[1][v1][v2] = 1
#                 queue.append((v1,v2))

# def three_bfs(i,j):
#     queue = deque()
#     queue.append((i,j))

#     while queue:
#         x, y = queue.popleft()
#         visited[0][x][y] = 1
#         for v1,v2 in three_color_graph[(x,y)]:
#             if visited[0][v1][v2] == 0:
#                 visited[1][v1][v2] = 1
#                 queue.append((v1,v2))

            
# for i in range(n):
#     for j in range(n):
#         if visited[0][i][j] == 0:
#             three_bfs(i,j)
#             three_cnt += 1
#         if visited[1][i][j] == 0:
#             two_bfs(i,j)
#             two_cnt += 1

# print(three_cnt,two_cnt)


# import sys
# input = sys.stdin.readline

# #<------------아직 푸는중~~_--------------
# n = int(input().rstrip())
# matrix = []
# visited = [[[0] * n for _ in range(n)] for _ in range(2)]
# three_color_graph, three_cnt = {}, 0
# two_color_graph, two_cnt = {}, 0
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# for i in range(n):
#     row = input().rstrip()
#     matrix.append(row)

# for i,row in enumerate(matrix):
#     for j,check in enumerate(row):
#         for k in range(4):
#             nx = i + dx[k]
#             ny = j + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if (i,j) not in three_color_graph:
#                     three_color_graph[(i,j)]=[]
#                 if (i,j) not in two_color_graph:
#                     two_color_graph[(i,j)]=[]

#                 if check == 'R':
#                     if matrix[nx][ny] == 'R':
#                         #색맹 아닐때
#                         three_color_graph[(i,j)].append((nx,ny))
#                         two_color_graph[(i,j)].append((nx,ny))
#                     if matrix[nx][ny] == 'G':
#                         #색맹일때
#                         two_color_graph[(i,j)].append((nx,ny))
                            
#                 elif check == 'G':
#                     if matrix[nx][ny] == 'G':
#                         three_color_graph[(i,j)].append((nx,ny))
#                         two_color_graph[(i,j)].append((nx,ny))
#                     if matrix[nx][ny] == 'R':
#                         #색맹일때
#                         two_color_graph[(i,j)].append((nx,ny))
                
#                 elif check == 'B':
#                     if matrix[nx][ny] == 'B':
#                         three_color_graph[(i,j)].append((nx,ny))
#                         two_color_graph[(i,j)].append((nx,ny))
# # print(two_color_graph)
# # print(three_color_graph)

# def dfs(k,i,j):
#     visited[k][i][j] = 1
#     if k==1:
#         for v1,v2 in two_color_graph[(i,j)]:
#             if visited[k][v1][v2]==0:
#                 visited[k][v1][v2] = 1
#                 dfs(k,v1,v2)
#             else:
#                 return 0
#     else:
#         for v1,v2 in three_color_graph[(i,j)]:
#             if visited[k][v1][v2]==0:
#                 visited[k][v1][v2] = 1
#                 dfs(k,v1,v2)
#             else:
#                 # print("[return 0]v1,v2",v1,v2)
#                 return 0

#     # print("[return 1]v1,v2",v1,v2)
#     return 1


# for i in range(n):
#     for j in range(n):
#         if visited[0][i][j] == 0:
#             three_cnt += dfs(0,i,j)
#         if visited[1][i][j] == 0:
#             two_cnt += dfs(1,i,j)


# # print(two_cnt)
# print(three_cnt,two_cnt)


