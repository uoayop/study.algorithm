# N-Queen
# https://www.acmicpc.net/problem/9663
# dfs, 백트래킹

# https://claude-u.tistory.com/245

import sys
input = sys.stdin.readline


# N x N에 N개의 퀸을 배치해야하므로 반드시 모든 행에 퀸이 들어가야 한다.
# 따라서 0열부터 N-1열까지 퀸을 놓는 방법을 for문으로 돌린다. (dfs)
# 이전 열에 겹치는 행이 있는지 체크해준다. (check)

def check(x):
    for i in range(x):
        # rows[x],  rows[i] --> 같은 열에 놓아져있는지 체크
        # abs(rows[x] - rows[i]) : abs(열 - 열), x-i : 행 - 행 --> 같은 대각선에 있는지 체크
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt

    if x == n:
        cnt += 1
    else:
        for i in range(n):
            rows[x] = i
            # (x,i)에 퀸을 놓고, 이전 행과 겹치지 않는지 체크해줌
            if check(x):
                # 겹치지 않으면 다음 행으로 이동
                dfs(x+1)

n = int(input())
rows = [0] * n
cnt = 0

dfs(0)
print(cnt)

# # ---------------- 나 이런게 못푸네
# import sys
# input = sys.stdin.readline

# dx = [-2, -2, 2, 2, -1, -1, 1, 1]
# dy = [1, -1, 1, -1, -2, 2, -2, 2]
# n = int(input())
# cnt = 0


# def dfs(m, x, y):
#     m -= 1
#     if m == 0:
#         return 1
#     print(x, y)
#     for row in maps:
#         print(row)
#     print()
#     if maps[x][y] == 0:
#         maps[x][y] = 1
#         for k in range(8):
#             nx = dx[k] + x
#             ny = dy[k] + y
#             if (0 <= nx < n and 0 <= ny < n):
#                 if maps[nx][ny] == 0:
#                     dfs(m, nx, ny)
#                     maps[x][y] = 0
#                 else:
#                     return 0
#     return 1


# maps = [[0] * n for _ in range(n)]
# if n == 1:
#     print(1)
# elif n < 4:
#     print(0)
# else:
#     for x in range(n):
#         for y in range(n):
#             answer = dfs(n, x, y)
#             print("answer>", x, y, answer)

# print(cnt)
