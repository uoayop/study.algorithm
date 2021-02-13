#이분그래프
#bfs
#https://www.acmicpc.net/problem/1707

import sys
from collections import deque
input = sys.stdin.readline


T = int(input().rstrip())
for _ in range(T):
    v,e = map(int,input().rstrip().rsplit())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        x,y = map(int,input().rstrip().rsplit())
        graph[x].append(y)
        graph[y].append(x)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v]=1

        while(queue):
            v = queue.popleft()
            for u in graph[v]:
                #print(u,visited)

                #정점 u를 방문 안했을 때
                if not visited[u]:
                    #정점 v의 그룹이 '-1'일때, 연결된 정점인 u의 그룹은 '1'/ '1'일땐 '-1'로 번갈아가면서 설정해준다.
                    if visited[v] == 1:
                        visited[u] = -1
                    elif visited[v] == -1:
                        visited[u] = 1
                    queue.append(u)
                    
                #정점 u는 방문했지만, 정점 v와 연결된 정점 u가 같은 그룹이면 NO를 출력한다.
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
    # print(dfs(1,0))