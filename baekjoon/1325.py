#효율적인 해킹
#bfs
#https://www.acmicpc.net/problem/1325


#<-------------pypy로 돌리면 통과되는데 그냥 파이썬으로 제출하면 시간초과 발생한다.
#왜 ...?

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited = [False] * (n+1)
    visited[v] = True
    cnt = 1

    while queue:
        target = queue.popleft()

        for new_target in graph[target]:
            if not visited[new_target]:
                queue.append(new_target)
                visited[new_target] = True
                cnt += 1
    return cnt

#n개의 컴퓨터, m개의 관계
n,m = map(int,input().rstrip().rsplit())
graph = [[] for _ in range(n+1)]
compare,answer, answer_list = 0, 0, []

queue = deque()

visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int,input().rstrip().rsplit())
    graph[b].append(a)

for i in range(1,len(graph)):
    if len(graph[i]) > 0:
        compare = bfs(i)
        if answer < compare:
            answer = compare
            answer_list = [i]
        elif answer == compare:
            answer_list.append(i)

for ans in answer_list:
    print(ans,end=" ")
print()
