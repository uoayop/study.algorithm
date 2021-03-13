# 숨바꼭질
# 최단거리
# https://www.acmicpc.net/problem/6118

import sys
from collections import deque
input = sys.stdin.readline
MAX_INT = 100000000

n, m = map(int,input().rstrip().rsplit())

graph = {}

for i in range(1,n+1):
    graph[i] = []

for _ in range(m):
    start, end = map(int,input().rstrip().rsplit())
    graph[start].append(end)
    graph[end].append(start)

q = deque()
q.append([1,0])

dist = [MAX_INT for _ in range(n+1)]
dist[1] = 0

answer = -1
answer_list = []

while q:
    key, cnt = q.popleft()
    for v in graph[key]:
        if dist[v] == MAX_INT:
            q.append([v,cnt+1])
        dist[v] = min(dist[v],cnt+1)

        if dist[v] > answer:
            answer = dist[v]
            answer_list = [v]
        elif dist[v] == answer:
            answer_list.append(v)

answer_list = list(set(answer_list))
print(min(answer_list), answer, len(answer_list))

