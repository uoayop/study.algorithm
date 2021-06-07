# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 그리디

import sys
input = sys.stdin.readline

order = input().rstrip()
# order = "1-2+3+4-5+2"
# order = "55-50+40"
# order = "50+50-100+100-100-100"
# order = "0-101-01"
sub1 = list(order.rsplit('-'))
# print(sub1)

first = True
for row in sub1:
    sub2 = list(map(int,''.join(row).rsplit('+')))

    print(sub2)
    if first:
        first = False
        temp = sum(sub2)
    else:
        temp -= sum(sub2)

print(temp)
