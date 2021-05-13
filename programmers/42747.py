# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    if max(citations) == 0:
        return 0
    
    for h in range(max(citations),0,-1):
        max_h = 0
        for c in citations:
            if c >= h:
                max_h += 1
            if max_h == h:
                return max_h

print(solution([2, 18, 22, 23]))