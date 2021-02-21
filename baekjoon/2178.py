#미로탐색
#bfs 최단거리
#http://www.acmicpc.net/problem/2178



#갈래가 한가지 이상 나오면, 모든 갈래를 queue에 넣어준다.
#이때 이미 갔던 곳이 나오면 방문하지 않는다. 
#한칸씩 이동할때마다 이동횟수를 1씩 증가하면서 넣어줬다.
#갈라졌던 갈래 중 도착지에 도착할때마다 min_num을 비교해줘서 더 작은 값을 저장한다.

import sys
from collections import deque                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
input = sys.stdin.readline

n, m = map(int,input().rsplit())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
graph, matrix = {}, []

for _ in range(n):
    row = input().rstrip()
    matrix.append(row)

for i,row in enumerate(matrix):
    for j,check in enumerate(row):
        if check == '1':
            graph[(i,j)]=[]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                        if matrix[nx][ny] == '1':
                            graph[(i,j)].append((nx,ny))

def bfs(graph,i,j):
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    queue = deque()
    queue.append([(i,j),1])

    while queue:
        temp = queue.popleft()
        location, cnt = temp[0], temp[1]

        if location == (n-1,m-1):
            return cnt
            
        if location not in visit:
            x, y =location[0], location[1]
            visit[x][y] = 1

            if location in graph:
                next_nodes = list(graph[location])

                for next_node in next_nodes:
                    x, y =next_node[0], next_node[1]
                    if visit[x][y]== 0:
                        queue.append([next_node,cnt+1])
                        visit[x][y] = 1

    
print(bfs(graph,0,0))
