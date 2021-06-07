# 전자레인지
# 그리디 알고리즘
# https://www.acmicpc.net/problem/10162

import sys

a, b, c = 300, 60, 10
T = int(sys.stdin.readline())

a_c = (T // a)
T %= a

b_c = (T // b)
T %= b

c_c = (T // c)
T %= c


if T != 0:
    print(-1)
else:
    print(a_c, b_c, c_c)