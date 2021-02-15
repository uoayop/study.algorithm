#특정 거리의 도시 찾기
#bfs
#https://www.acmicpc.net/problem/18352


# <--------BFS------------>
# import sys
# from collections import deque
 
# input = sys.stdin.readline

# # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# n,m,k,x = map(int,input().rstrip().rsplit())
# visited = [False] * (n+1)
# graph = [[] for _ in range(n+1)]
# result = []

# for _ in range(m):
#     a,b = map(int,input().rstrip().rsplit())
#     graph[a].append(b)

# Q = deque()
# Q.append((0,x))
# visited[x]=False

# while Q:
#     time,node = Q.popleft()
#     for v in graph[node]:
#         # 방문하지 않은 노드일때만 거리를 +1 해서 큐에 넣어준다.
#         if not visited[v]:
#             visited[v] = time + 1
#             Q.append((time+1, v))

# for i in range(len(visited)):
#     if visited[i]==k:
#         result.append(i)

# if len(result)==0:
#     print(-1)

# elif len(result)==1:
#     if x==result[0] and k!=0:
#         print(-1)
#     else:
#         result.sort()
#         for num in result:
#             print(num)
# else:
#     result.sort()
#     for num in result:
#         print(num)


# <--------다익스트라------------>
import sys
import heapq
import collections
input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n,m,k,x = map(int,input().rstrip().rsplit())
graph = [[] for _ in range(n+1)]
result = []

for _ in range(m):
    a,b = map(int,input().rstrip().rsplit())
    graph[a].append((b,1))

Q = [(0,x)]
dist = collections.defaultdict(int)

while Q:
    time,node = heapq.heappop(Q)
    if node not in dist:
        dist[node]=time
        for v,w in graph[node]:
            heapq.heappush(Q,(time+1,v))
        if time==k:
            result.append(node)

if len(result)==0:
    print(-1)

elif len(result)==1:
    if x==result[0] and k!=0:
        print(-1)
    else:
        result.sort()
        for num in result:
            print(num)
else:
    result.sort()
    for num in result:
        print(num)