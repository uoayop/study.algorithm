#버블 정렬
#https://www.acmicpc.net/problem/1838

# 문제의 i가 의미하는 것 
# = 더 이상 정렬을 하지 않아도 되서 멈췄을 때, 몇번 정렬이 이루어졌는지
# 버블 정렬은 정렬을 한번씩 할때마다 가장 큰 값이 가장 뒤로 이동함
# 따라서 [뒤로 이동한 값] 중 [가장 많이 이동한 거리]를 찾으면 됨

# 정답 = [정렬 전 인덱스 - 정렬 후 인덱스 > 0] 중 가장 큰 값

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().rsplit()))

before = defaultdict(int)
for i,num in enumerate(a):
    before[num]=i

a.sort()

after = defaultdict(int)
for i,num in enumerate(a):
    after[num] = i

answer = 0
for num in before:
    minus = before[num] - after[num]
    if ( minus > 0 and minus > answer):
        answer = minus

print(answer)
# print(a)