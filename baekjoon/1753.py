#최단경로
#다익스트라 알고리즘
#https://www.acmicpc.net/problem/1753

import sys
import collections
import heapq

input = sys.stdin.readline


# 정점 개수 v, 간선 개수 e, 시작정점 k
vc, ec = map(int,input().rstrip().rsplit())
k = int(input().rstrip())
graph = collections.defaultdict(list)

for _ in range(ec):
    u, v, w = map(int,input().rstrip().rsplit())
    graph[u].append((v,w))

Q = [(0,k)]
dist = collections.defaultdict(int)
while Q:
    cnt, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = cnt
        for v,w in graph[node]:
            # temp : 현재 정점까지 오는데에 걸린 경로 + 가중치
            temp = cnt + w
            heapq.heappush(Q,(temp,v))

# dist 리스트에 저장된 가중치 값을 출력해준다
# 이때 시작점이 아닌데 가중치가 0인값은 경로가 존재하지 않는 경우이므로 INF를 출력한다.
for i in range(1,vc+1):
    if dist[i]==0 and i!=k:
        print("INF")
    else:
        print(dist[i])