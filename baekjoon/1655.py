# 가운데를 말해요
# 힙
# https://www.acmicpc.net/problem/1655

'''
왼쪽 힙 left(max heap), 오른쪽 힙 right(min heap)을 사용해서 중간값 관리하기
len(left) == len(right) 이면 무조건 left에 삽입
이외에는 right에 삽입한다.
만약 left의 가장 큰 값(max_h[0][1])이 right의 가장 작은 값(min_h[0][1])보다 더 크면 값을 바꿔준다.
이렇게 되면 right의 가장 큰 값은 중간값이 된다.

https://jjangsungwon.tistory.com/87
'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_h, min_h = [], []

for i in range(n):
    num = int(input())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    print("max_h",max_h,"min_h",min_h)
    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0] * -1 > min_h[0]:
        max_value = heapq.heappop(max_h) * -1
        min_value = heapq.heappop(min_h)
        
        heapq.heappush(max_h, min_value * -1)
        heapq.heappush(min_h, max_value)

    print(">",max_h[0] * -1)

# 시간초과~~~ ㅎ

# for i in range(n):
#     num = int(input())
#     heapq.heappush(h, num)
#     if len(h) < 3:
#         print("a:",(h[0]))
#     else:
#         k = ((len(h) + 1) // 2)
#         hc = h.copy()
#         for _ in range(k-1):
#             heapq.heappop(hc)
#         print("a:",heapq.heappop(hc))
