# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    common = 0
    for i in range(min(w,h), 1, -1):
        if w % i == 0 and h % i == 0:
            common = i
            break
    
    # 최대 공약수 common
    # 대각선 사각형의 범위 가로 x, 세로 y
    x = w // common
    y = h // common

    # 망가지는 사각형의 수는 (x + y -1) * common 개
    return w * h - ((x + y - 1) * common)

print(solution(8, 12))