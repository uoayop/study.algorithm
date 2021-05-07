#바이러스
#https://www.acmicpc.net/problem/2606

import sys

computer = int(sys.stdin.readline().rstrip())
connect = int(sys.stdin.readline().rstrip())
visited = [0] * (computer + 1)
total = 0
graph = {}

for i in range(connect):
    key, value = map(int,sys.stdin.readline().rstrip().rsplit())

    #양방향으로 그래프 만들어주기
    if key not in graph:
        graph[key]=[value]
    else:
        graph[key].append(value)

    if value not in graph:
        graph[value]=[key]
    else:
        graph[value].append(key)

def dfs(index):
    #방문한 적 없으면
    if visited[index] == 0:
        visited[index] = 1

        while(graph[index]):
            dfs(graph[index].pop(0))

dfs(1)

for num in visited:
    if num==1: 
        total += 1

print(total-1)