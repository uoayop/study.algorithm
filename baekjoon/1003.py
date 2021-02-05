#피보나치 함수
#다이나믹 프로그래밍
#https://www.acmicpc.net/problem/1003

import sys

dp = [0] * 41

def fibo(n):
    if dp[n] != 0:
        return dp[n]
    if n<2:
        return n
    else:
        dp[n] = fibo(n-1)+fibo(n-2)
        return dp[n]

T=int(sys.stdin.readline())

for i in range(T):
    case = int(sys.stdin.readline())
    
    if case == 0:
        print(1,0)
    elif case == 1:
        print(0,1)
    else:
        print(fibo(case-1),fibo(case))