# 주유소
# 그리디 알고리즘
# https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int,input().rsplit()))
price = list(map(int,input().rsplit()))

answer = 0
min_price = price[0]
for i in range(n-1):
    min_price = min(min_price, price[i])
    answer += (length[i] * min_price)

print(answer)
    
