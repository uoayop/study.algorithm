# 위장
# 해시
# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict

def solution(clothes):
    dct = defaultdict(int)
    for cloth, kinds in clothes:
        dct[kinds] += 1

    answer = 1
    for k, v in dct.items():
        answer *= (v + 1)
    print(answer-1)



solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])

solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
