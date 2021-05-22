# 가장 긴 증가하는 부분수열2
# https://www.acmicpc.net/problem/12015
# 이분탐색


# # dp : 시간초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().rsplit()))

# # dp[i] = 배열의 i번째까지 만들 수 있는 가장 긴 수열의 길이
# dp = [1] * n

# for i in range(n):
#     for j in range(i):
#         if a[j] < a[i]:
#             dp[i] = max(dp[j]+1, dp[i])

# print(max(dp))


# dp 중 특별케이스인 lis : 가장 긴 증가하는 부분 수열
# https://jason9319.tistory.com/113

'''
1. 세그먼트 트리 사용
arr[x]의 위치에 x번째 수를 마지막 원소로 가지는 Lis의 길이를 업데이트하기
매 순간마다 자기보다 작은 구간에 최댓값을 찾아서 +1 해줌

2. 이분 탐색 사용
= 최적의 위치에 수 삽입하기
Lis 수열을 하나 만들고, 가장 맨 뒤에 있는 원소보다 arr의 값이 더 크면 
Lis에 넣어주고, Lis 크기를 1 증가시킴

만약 arr의 원소가 Lis 가장 맨 뒤에 있는 원소보다 작을 경우
lower_bound 를 이용해 최적의 자리를 찾아서 값을 교체해버림
'''

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rsplit()))
lis = []
ans = 0

for num in a:
    if not lis:
        lis.append(num)
        ans += 1
        continue
    
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    else:
        index = bisect_left(lis, num)
        lis[index] = num
    # print(lis,num,ans)
    
print(ans)

