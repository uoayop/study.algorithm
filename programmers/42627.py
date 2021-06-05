# 디스크 컨트롤러
# 힙
# https://programmers.co.kr/learn/courses/30/lessons/42627

import sys
import heapq
from collections import deque


def solution(jobs):
    answer = 0
    h = []
    curr = sys.maxsize
    temp = []
    for j in jobs:
        heapq.heappush(h, (j[1], j[0]))
        if j[0] < curr:
            curr = j[0]

    # print(curr)
    while h:
        # 작업이 끝난 뒤 실행 될 다음 작업이
        # 현재 시점보다 뒤에 있을 수 있다!
        # print(arrived, time)
        while h and curr < h[0][1]:
            time, arrived = heapq.heappop(h)
            heapq.heappush(temp,(time,arrived))
        if not h:
            curr += 1
        else:
            time, arrived = heapq.heappop(h)
            curr += time
            answer += (curr - arrived)
            
        while temp:
            t = heapq.heappop(temp)
            heapq.heappush(h, t)

        # print("[curr]",curr,"[arrived]", arrived)
    
    
    return (answer//len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))
