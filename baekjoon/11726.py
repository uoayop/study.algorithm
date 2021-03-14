#2xn 타일링
#https://www.acmicpc.net/problem/11726
#DP
 
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())

nums = [0] * (n+1)
def tile(n):
    if n==1:
        return 1
    elif n==2:
        return 2

    if nums[n]:
        return nums[n]
    else:
        nums[n] = tile(n-1) + tile(n-2)
        return nums[n]

print(tile(n)%10007)
