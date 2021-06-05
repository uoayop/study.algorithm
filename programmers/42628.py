# 이중우선순위큐
# 힙
# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq


def solution(operations):

    print('----------------------')
    l, r = [], []

    def compare(s, t):
        if s and t:
            if len(s) > len(t):
                heapq.heappush(t, heapq.heappop(s) * -1)
            elif len(s) < len(t):
                heapq.heappush(s, heapq.heappop(t) * -1)
        return (s, t)

    for row in operations:
        print(l, r)
        opr, num = row.rsplit()
        if opr == 'I':
            if len(l) == len(r):
                heapq.heappush(l, int(num))
            else:
                heapq.heappush(r, -1 * int(num))

            if l and r:
                if l[0] > -r[0]:
                    left = heapq.heappop(l)
                    right = heapq.heappop(r)

                    heapq.heappush(l, -1 * right)
                    heapq.heappush(r, -1 * left)
        else:
            l, r = compare(l, r)
            if num == '1':
                if r:
                    heapq.heappop(r)
            else:
                if l:
                    heapq.heappop(l)
            l, r = compare(l, r)

    print(l, r)
    if not l and not r:
        return [0, 0]

    min, max = 0, 0
    l, r = compare(l, r)
    if l:
        min = heapq.heappop(l)
    if r:
        max = heapq.heappop(r) * -1

    return [max, min]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
