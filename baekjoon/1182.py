# 부분 수열의 합
# https://www.acmicpc.net/problem/1182
# 백트래킹, 브루트포스

import sys
input = sys.stdin.readline

total_cnt = 0

def dfs(index, n, s, cnt):
    global total_cnt
    if index == n: 
        return
    if cnt + nums[index] == s:
        total_cnt += 1
    dfs(index+1, n, s, cnt) # 0 
    dfs(index+1, n, s, cnt + nums[index]) # num

n, s = map(int, input().rsplit())
nums = sorted(list(map(int, input().rsplit())))

dfs(0, n, s, 0)

print(total_cnt)

# # 못품..
# def dfs(length, sum, depth):
#     result = []
#     if (length == depth):
#         if sum == s:
#             return 1
#         return 0

#     for i in range(length):
#         for j in range(i+1, n):
#             print(nums[i], nums[j])
#             dfs(length, sum + nums[j], depth+1)

#     return 0


# cnt = 0
# # n : 1,2,3,4,5
# for i in range(1, n+1):
#     print(">>i :", i)
#     cnt += dfs(i, 0, 0)

# print(cnt)
