#설탕배달
#DP
#https://www.acmicpc.net/problem/2839

import sys
input= sys.stdin.readline

n = int(input().rstrip())

def delivery(n,cnt):
    while True:
        if n % 5 == 0:
            cnt = cnt + n//5
            return cnt
        
        n -= 3
        cnt += 1

        if n<0:
            return -1

        
print(delivery(n,0))
