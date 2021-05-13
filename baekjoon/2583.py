# 영역 구하기
# https://www.acmicpc.net/problem/2583

import sys
from collections import defaultdict
sys.setrecursionlimit(100001)
input = sys.stdin.readline

m, n, k = map(int, input().rsplit())

maps = [[0 for _ in range(n)] for _ in range(m)]
dst = defaultdict(list)

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().rsplit())
    for i in range(x1, x2):
        for j in range(y1, y2):
            maps[i][j] = 1

# for row in maps:
#     print(row)
# print()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x, rows in enumerate(maps):
    for y, char in enumerate(rows):
        if char == 0:
            dst[(x, y)].append((x, y))
            for t in range(4):
                nx = dx[t] + x
                ny = dy[t] + y
                if (0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 0):
                    dst[(x, y)].append((nx, ny))

# print(dst)

cnt = 0


def dfs(x, y):
    global cnt

    cnt += 1
    if maps[x][y] == 0:
        maps[x][y] = 1

        for (nx, ny) in dst[(x, y)]:
            if maps[nx][ny] == 0:
                dfs(nx, ny)
    else:
        return False
    return cnt

ground = 0
result = []

for x, y in dst:
    cnt = 0
    answer = dfs(x, y)
    if answer:
        ground += 1
        result.append(answer)

result.sort()
print(ground)
print(' '.join(map(str,result)))