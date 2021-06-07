# 캠핑
# 그리디
# https://www.acmicpc.net/problem/4796

import sys
input = sys.stdin.readline


i = 1
while 1:
    l, p, v = map(int,input().rsplit())
    ans = 0
    if l == 0 and p == 0 and v == 0:
        break

    ans += (v // p) * l
    if v % p > l:
        ans += l
    else:
        ans += v % p

    print("Case {0}: {1}".format(i,ans))
    i += 1