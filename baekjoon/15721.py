# 번데기
# https://www.acmicpc.net/problem/15721
# 구현

import sys
input = sys.stdin.readline

# 게임 진행하는 사람 a명, t번째 구호 외치는 사람 위치 출력
# 원하는 구호가 '뻔'이면 0, '데기'면 1
a = int(input())
t = int(input())
want = int(input())
round, cnt, result = 0, 0, 0

while True:
    round += 1
    lst = [0, 1, 0, 1]  # 뻔, 데기, 뻔, 데기
    for i in range(round+1): lst.append(0)
    for i in range(round+1): lst.append(1)

    for index,value in enumerate(lst):
        if value == want: cnt+=1
        if cnt==t:
            print(result)
            exit(0)
        result += 1
        result %= a