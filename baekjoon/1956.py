# #운동
# #https://www.acmicpc.net/problem/1956
# #최단거리

# import sys
# from collections import deque
# input = sys.stdin.readline
# MAX_INT = 99999999

# #v개의 마을, e개의 도로
# v, e = map(int,input().rstrip().rsplit())
# cost=[[-1]*(v+1) for _ in range(v+1)]
# dist = [[MAX_INT for _ in range(v+1)] for _ in range(v+1)]
# city = {}
# min_cycle = MAX_INT

# for _ in range(e):
#     a,b,c = map(int,input().rstrip().rsplit())
#     cost[a][b] = c
    
#     if a not in city:
#         city[a]=[b]
#     else:
#         city[a].append(b)

# for start in city:
#     visited = [False for _ in range(v+1)]
#     print("-------------------\n[start]",start)
#     q = deque()
#     q.append(start)

#     cnt = 0
#     min_cycle = MAX_INT
#     while q:
#         visited[start] = False
#         curr = q.popleft()
#         print("[curr]",curr)
#         if curr == start:
#             if cnt!=0:
#                 min_cycle = min(min_cycle,cnt)
#             print("[min_cycle]",min_cycle)

#         for next in city[curr]:
#             if not visited[next]:
#                 visited[next] = True
#                 cnt += cost[curr][next]
#                 print("[cnt]",cnt)
#                 q.append(next)

# if min_cycle==MAX_INT:
#     print(-1)
#     sys.exit(0)
# else:
#     print(min_cycle)

#운동
#https://www.acmicpc.net/problem/1956
#최단거리

import sys
from collections import deque
input = sys.stdin.readline
MAX_INT = 99999999

#v개의 마을, e개의 도로
v, e = map(int,input().rstrip().rsplit())
dist = [[MAX_INT for _ in range(v+1)] for _ in range(v+1)]
min_cycle = MAX_INT

for _ in range(e):
    a,b,c = map(int,input().rstrip().rsplit())
    dist[a][b] = c

for k in range(1,v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            dist[i][j] = min(
                dist[i][j], 
                dist[i][k] + dist[k][j]
            )
   
for i in range(1, v+1):
    min_cycle = min(min_cycle, dist[i][i])

if min_cycle==MAX_INT:
    print(-1)
    sys.exit(0)
else:
    print(min_cycle)