#게임 맵 최단거리
#https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
from collections import defaultdict

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    print("n",n,"m",m)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    graph = defaultdict(list)
    for i,row in enumerate(maps):
        for j,check in enumerate(row):
            if check == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if maps[nx][ny] == 1:
                            graph[(i,j)].append((nx,ny))
                            graph[(nx,ny)].append((i,j))

    def bfs(graph,i,j):
        visit = [[0] * m for _ in range(n)]
        visit[0][0] = 1
        queue = deque()
        queue.append([(i,j),1])

        while queue:
            print(queue)
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
    
    # answer = 0
    # return answer

solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])