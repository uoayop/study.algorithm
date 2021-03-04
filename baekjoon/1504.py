#특정한 최단 경로
#https://www.acmicpc.net/problem/1504
#다익스트라

import sys
import heapq

input = sys.stdin.readline
MAX_INT = sys.maxsize

def dijkstra(start):
    distance = [MAX_INT for _ in range(n+1)]
    q = [start] # [비용,시작점]
    
    # 자기 자신의 거리 0으로 만들기
    distance[start[1]] = 0
    while q:
        p = heapq.heappop(q)
        cur_cost, cur_location = p[0], p[1]
        # print("[cost,now]:",cost,now)
        # 현재 위치한 정점과 연결된 정점 Next 들 방문
        for next_cost, next_location in graph[cur_location]:
            # (연결된 정점으로 이동 비용) vs (현재 비용 + 이동 비용): 비교해서 더 작은 값으로 재할당 해줌
            # print("[Next_cost,Next]:",Next_cost,Next)
            if distance[next_location] > cur_cost + next_cost:
                distance[next_location] = cur_cost + next_cost
                # print("[distance]",distance)
                heapq.heappush(q,[distance[next_location],next_location])
    return distance

n,e = map(int,input().rstrip().rsplit())
graph = [[] for _ in range(n+1)] 
for _ in range(e):
    a, b, c = map(int,input().rstrip().rsplit())
    # graph[출발지] = [비용,도착지]
    graph[a].append([c,b])
    graph[b].append([c,a])
# 경유지 v1, v2 
v1, v2 = map(int,input().rstrip().rsplit())

go = dijkstra([0,1])
v1go = dijkstra([0,v1])
v2go = dijkstra([0,v2])

answer = (min(go[v1]+v1go[v2]+v2go[n],go[v2]+v2go[v1]+v1go[n]))
if answer >= MAX_INT:
    print(-1)
else:
    print(answer)

#<---------- 에러 코드------------>
# import sys
# input = sys.stdin.readline
# MAX_INT = sys.maxsize

# n,e = map(int,input().rstrip().rsplit())
# graph = [[ 0 for _ in range(n+1) ] for _ in range(n+1)]
# for _ in range(e):
#     a, b, c = map(int,input().rstrip().rsplit())
#     if graph[a][b]==0 or graph[a][b] > c:
#         graph[a][b] = c
#         graph[b][a] = c

# v1, v2 = map(int,input().rstrip().rsplit())

# path1 = [1, v1, v2, n]
# path2 = [1, v2, v1, n]

# answer1 = 0
# answer2 = 0
# answer = 0

# for i in range(0,3):
#     now_n = path1[i]
#     next_n = path1[i+1]

#     if graph[now_n][next_n]==0:
#         answer1 = -1
#         break
#     answer1 += graph[now_n][next_n]

# for i in range(0,3):
#     now_n = path2[i]
#     next_n = path2[i+1]

#     if graph[now_n][next_n]==0:
#         answer2 = -1
#         break
#     answer2 += graph[now_n][next_n]
    
# if answer1 == -1 and answer2 == -1:
#     print(-1)
# elif answer == -1 and answer2!= -1:
#     print(answer2)
# elif answer != -1 and answer2== -1:
#     print(answer1)
# elif answer != -1 and answer2 != -1:
#     print(min(answer1,answer2))


