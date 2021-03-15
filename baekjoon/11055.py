#가장 큰 증가 부분 수열
#https://www.acmicpc.net/problem/11055
#dp

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = ['dummy']
dp = ['dummy']
# dp[i] = arr[i]를 가장 큰 값으로 가지는 수열의 합

nums = input().rstrip().rsplit()
for num in nums:
    arr.append(int(num))
    dp.append(int(num))

memo = 0

for i in range(1,n+1):
    for j in range(1,i):
        print(dp)
        # 비교값(arr[j])이 현재값(arr[i])보다 작고(;증가 수열), 
        # 비교값을 마지막 값으로 갖는 수열의 합과 현재값을 더한 값이 
        # 현재 수열의 합보다 크면 갱신해준다.
        if arr[i] > arr[j] and dp[j] + arr[i] > dp[i]:
            dp[i] = dp[j] + arr[i]
    
    # 최대값을 저장해준다.
    if memo < dp[i]:
        memo = dp[i]

print(memo)