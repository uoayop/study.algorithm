# 날짜 계산
# https://www.acmicpc.net/problem/1476
# 구현

import sys
from typing import Tuple
input = sys.stdin.readline

E, S, M = map(int,input().rsplit())
# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
e, s, m = 0, 0, 0
answer = 0

while True:
    e %= 15
    s %= 28
    m %= 19

    e+=1 
    s+=1
    m+=1

    answer += 1

    if (E==e and S==s and M==m): 
        print(answer)
        exit(0)