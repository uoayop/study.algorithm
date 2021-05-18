# 보물
# https://www.acmicpc.net/problem/1026
# 정렬

import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []

a = sorted(list(map(int,input().rsplit())))
b = sorted(list(map(int,input().rsplit())),reverse=True)

sum = 0
for i in range(n):
    sum += (a[i]*b[i])

print(sum)