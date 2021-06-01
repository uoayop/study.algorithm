# 게으름 백곰
# 투포인터
# https://www.acmicpc.net/problem/10025

import sys
from collections import defaultdict
input = sys.stdin.readline

# n개의 얼음 양동이들이 좌표마다 놓여있다.
# 앨버트는 좌우로 k만큼 떨어진 양동이까지 닿을 수 있다.
# 최적의 자리를 골랐을 때 얼음의 합

# left, right : 양동이가 위치한 가장 좌측과 우측
# start, end : 투 포인터
# curr : 현재 얼음의 양

# 툭정 좌표 x에서 [x-k, x+k] 까지의 범위를 확인해야 한다.
# 따라서 end - start 가 k*2 이하일 때까지 end를 증가시키면 된다.
# 얼음의 양 갱신 후 curr에서 좌측 포인터의 원소값 ice[start]를 빼준다.

n, k = map(int,input().rsplit())
ice = defaultdict(int)
min_l, max_l, answer = sys.maxsize, 0, -1

for _ in range(n):
    g, x = map(int,input().rsplit())
    ice[x] = g
    max_l = max(max_l, x)
    min_l = min(min_l, x)

# while left + (2*k) <= max_l:
#     curr = 0
#     for i in range(2*k):
#         curr += ice[min_l + i]
#     print(left, curr, answer)
#     answer = max(answer, curr)
#     left += 1

# print(answer)

end, curr = min_l, 0
for start in range(min_l, max_l + 1):
    while end < max_l + 1 and end - start <= k * 2:
        if ice[end] == 0:
            end += 1
            continue
        curr += ice[end]
        end += 1
    answer = max(answer, curr)
    curr -= ice[start]
    
    # while r <= l + k and r < max_l and curr > answer:
    #     curr += ice[r]
    #     r += 1
    # print(l, r, curr, answer)
    # answer = max(curr, answer)
    # curr -= ice[l]

print(answer)

'''
4 3
7 8 6
3 0 0
4 6 0
1 4 2

8

'''