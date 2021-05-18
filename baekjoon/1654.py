# 랜선 자르기
# https://www.acmicpc.net/problem/1654
# 이진 탐색

import sys
input = sys.stdin.readline

# 이미 가지고 있는 k개의 랜선, n개의 랜선 필요
# n개(또는 n개보다 많이) 를 만들 수 있는 랜선의 최대 길이

k, n = map(int,input().rsplit())
lans = []
for _ in range(k):
    lans.append(int(input()))

l, r = 1, max(lans)
result = 0

while l <= r:
    mid = ((l + r) // 2 if (l + r) // 2 !=0 else 1)
    check = sum(l // mid if l >= mid else 0 for l in lans)
    print("check:{0}, mid:{1}, l:{2}, r:{3}".format(check,mid,l,r))
    if check >= n:
        l = mid + 1
        result = max(result, mid)
    else:
        r = mid - 1

print(result)
    
