# 부분합
# 투포인터
# https://www.acmicpc.net/problem/1806

import sys
input = sys.stdin.readline

n, s = map(int,input().rsplit())
nums = list(map(int,input().rsplit()))

# n개의 숫자 중 연속된 부분합 중에 그 합이 s 이상이 되는 가장 짧은 것의 길이
# https://paris-in-the-rain.tistory.com/127

l, r = 0, 0
answer = sys.maxsize
hap = 0

while (1):
    if hap >= s:
        answer = min(answer, r - l)
        hap -= nums[l]
        l += 1

    elif r == n:
        break

    else:
        hap += nums[r]
        r += 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)