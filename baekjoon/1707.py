#이분그래프
#bfs
#https://www.acmicpc.net/problem/1707

import sys
from collections import deque
input = sys.stdin.readline

# 테스트케이스 개수 T
T = int(input().rstrip())

for _ in range(T):
    # 정점 개수 v, 간선 개수 e
    v,e = map(int,input().rstrip().rsplit())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        # 연결된 간선 x,y
        x,y = map(int,input().rstrip().rsplit())
        graph[x].append(y)
        graph[y].append(x)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = 1

        while(queue):
            v = queue.popleft()
            for u in graph[v]:
                #print(u,visited)

                #정점 u를 방문 안했을 때
                if not visited[u]:
                    #정점 v와 연결된 정점인 u의 그룹은 서로 다르게 설정한다.
                    if visited[v] == 1:
                        visited[u] = -1
                    elif visited[v] == -1:
                        visited[u] = 1
                    queue.append(u)
                    
                #정점 u는 방문했지만, 정점 v와 u가 같은 그룹이면 NO를 출력한다.
                elif visited[u] == visited[v]:
                    return 0
        return 1
        
    check = False
    for i in range(v):
        #방문하지 않은 노드만 bfs로 호출해서 들어가기
        if visited[i]==0:
            ans = bfs(i)
            if ans == 0 :
                check = True
                break

    if check == True:
        print("NO")
    else:
        print("YES")