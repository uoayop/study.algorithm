#통계학
# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

# 산술평균 avg
def avg(arr):
    hap = sum(arr)
    return hap//len(arr)

# 중앙값 mid
def mid(arr):
    arr = sorted(arr)
    mid = len(arr)//2
    return arr[mid]

# 최빈값 freq
def freq(arr):
    if len(arr) == 1:
        return arr[0]

    arr = sorted(arr)
    c = Counter(arr)
    # first = 가장 빈도수가 큰 값 1개 [(값, 빈도수)]
    first = c.most_common(1)
    # second = 가장 빈도수가 큰 값 2개 [(값, 빈도수), (값, 빈도수)]
    second = c.most_common(2)

    # 빈도수가 같으면 두번째로 작은 값 출력
    if first[0][1] == second[1][1]: return second[1][0]
    return first[0][0]

# 범위 ran
def ran(arr):
    return max(arr) - min(arr)


n = int(sys.stdin.readline())
num = []

for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    num.append(temp)

print(avg(num))
print(mid(num))
print(freq(num))
print(ran(num))