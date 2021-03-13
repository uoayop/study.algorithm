#RGB거리
#https://www.acmicpc.net/problem/1149
#DP

# # <---------욕심쟁이 알고리즘 (틀림)
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# sum = 0
# memo = -1

# def mincheck(RGB):
#     m = 1000001
#     mi = 0
#     for index,color in enumerate(RGB):
#         if m > color:
#             m = color
#             mi = index
#     return mi,m

# for i in range(n):
#     RGB = list(map(int,input().rstrip().rsplit()))
    
#     min_index, min = mincheck(RGB)
    
#     if min_index == memo:
#         RGB[min_index] = 1000001
#         min_index, min = mincheck(RGB)

#     sum += min
#     memo = min_index

# print(sum)
   
    
import sys
input = sys.stdin.readline

n = int(input().rstrip())
colors = []

for i in range(n):
    RGB = list(map(int,input().rstrip().rsplit()))
    colors.append(RGB)

memo = [[] for _ in range(n)]
memo[0] = colors[0]

#f(n) = min (
# f(r) + min[f(n-1,b),f(n-1,g) ,
# f(g) + min[f(n-1,r),f(n-1,b) ,
# f(b) + min[f(n-1,r),f(n-1,g)]
#)

for i in range(1,n):
    memo[i] = [
        colors[i][0] + min(memo[i-1][1],memo[i-1][2]),
        colors[i][1] + min(memo[i-1][0],memo[i-1][2]),
        colors[i][2] + min(memo[i-1][0],memo[i-1][1]),
    ]

print(min(memo[n-1]))

    
