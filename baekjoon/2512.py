# 예산
# https://www.acmicpc.net/problem/2512
# 이진 탐색

import sys
input = sys.stdin.readline

n = int(input())
moneys = list(map(int,input().rsplit()))
goal = int(input())

def checking(highest_m):
    hap = sum(highest_m if highest_m < m else m for m in moneys)
    return hap

l, r = goal // n, max(moneys)
answer = 0
while l <= r:
    mid = (l + r) // 2
    # 더한 금액이 goal보다 같거나 크므로 상한액 줄여주기
    temp = checking(mid)
    print("answer:{0}, mid:{1}, l:{2}, r:{3}".format(temp,mid,l,r))
    if checking(mid) > goal:
        r = mid - 1
    else:
        answer = max(answer, mid)
        l = mid + 1

print(answer)