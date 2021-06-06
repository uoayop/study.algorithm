# 카펫
# 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    xy = brown + yellow
    # 가로 x, 세로 y
    for x in range(3, xy + 1):
        for y in range(x, 1, -1):
            if x < y:
                continue
            elif x * y == xy:
                if 2 * x + 2 * (y-2) == brown:
                    return [x,y]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(14, 4))
print(solution(18, 6))