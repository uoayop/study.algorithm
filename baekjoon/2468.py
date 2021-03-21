#안전영역
#https://www.acmicpc.net/problem/2468
#dfs, bfs

import sys
import heapq
from collections import deque
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

# n행, n열

# heights : 영역의 높이를 입력받다가 없으면 입력 받기
# 그 높이를 한개씩 꺼내와서, 그 높이보다 낮은 영역이 있으면 방문 체크 해주기
# 방문 체크가 안된 지역의 개수를 세어주자

n = int(input().rstrip())
ground = []
heights = []
max_count = []

for _ in range(n):
    row = list(map(int,input().rstrip().rsplit()))
    ground.append(row)
    for char in row:
        if char not in heights:
            heapq.heappush(heights, char)

def dfs(x, y, check):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y

        if (0 <= nx < n) and (0<=ny<n) and not visited[nx][ny] and ground[nx][ny] > check:
            visited[nx][ny] = True
            dfs(nx, ny, check)

for i in range(len(heights)):
    q = deque((0,0))
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    check = heapq.heappop(heights)

    num = 0
    for j in range(n):
        for k in range(n):
            if ground[j][k] > check and not visited[j][k]:
                num += 1
                visited[j][k] = True
                dfs(j, k, check)

    max_count.append(num)

answer = max(max_count)
# 예외처리 : 아무 지역도 잠기지 않을 때 지여의 개수는 1
if answer == 0:
    print(1)
else:
    print(answer)