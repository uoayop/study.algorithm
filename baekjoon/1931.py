# 회의실 배정
# 그리디
# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())
# n = 11
times = sorted([list(map(int,input().rsplit())) for _ in range(n)], key=lambda x: (x[1],x[0]))
# times = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

# print(times)


start, end = times[0]
cnt = 1
for i in range(1, n):
    n_start, n_end = times[i]
    if end <= n_start:
        start, end = n_start, n_end
        cnt += 1

print(cnt)

# 시간 초과
# answer = 0
# for i in range(n):
#     index, temp = i, [(times[i])]
#     j = i + 1
#     while j < n:
#         start, end = times[index]
#         n_start, n_end = times[j]

#         if end > n_start:
#             j += 1
#         else:
#             temp.append((n_start, n_end))
#             index = j
#             j = index + 1
    
#     answer = max(answer, len(temp))

# print(answer)

