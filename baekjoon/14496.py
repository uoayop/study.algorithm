#그대, 그머가 되어
#다익스트라 알고리즘 : 최단거리
#https://www.acmicpc.net/problem/14496

import sys
import collections
import heapq

input = sys.stdin.readline

#바꾸려 하는 문자 a,b 
a, b = map(int,input().rstrip().rsplit())
#전체 문자의 수 n, 치환 가능한 문자쌍의 수 m
n, m = map(int,input().rstrip().rsplit())
graph = collections.defaultdict(list)
check = False
answer = 0

for _ in range(m):
    x, y = map(int,input().rstrip().rsplit())
    #양방향으로 연결해줘야한다. (ex)멍멍이 <-> 댕댕이
    graph[x].append(y)
    graph[y].append(x)

Q = [(0,a)]
dist = collections.defaultdict(int)
while Q:
    cnt, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = cnt
        for v in graph[node]:
            heapq.heappush(Q,(cnt+1,v))
        if node == b:
            check = True
            answer = cnt
            break

if check:
    print(answer)
else:
    print(-1)