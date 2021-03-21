#안녕
#dp, 배낭 문제
#https://www.acmicpc.net/problem/1535


# # ---------------dp 틀림
# # 사람의 수 n
# n = int(input())
# lose = list(map(int,input().split()))
# happy = list(map(int,input().split()))

# dp = [0] * 101
# # dp[i] 배열은 체력이 i일때 얻을 수 있는 가장 큰 기쁨이 저장된다.

# max_happy = 0
# # for index,value in enumerate(lose):
# #     new_hp = current_hp - value
# #     if new_hp < 0:
# #         continue
    
# #     current_hp -= value
# #     dp[new_hp] = max(dp[new_hp], dp[current_hp]+happy[index])

# for i in range(n):
#     current_hp = 100
#     for j in range(i,n):
#         new_hp = current_hp - lose[j]
#         if new_hp <= 0 :
#             break

#         dp[new_hp] = max(dp[current_hp]+happy[j], dp[new_hp]) 
#         current_hp -= lose[j]
        
#         max_happy = max(max_happy, dp[new_hp])

# print(max_happy)


# # 냅색 정답 ----------------------------
# # 사람의 수 n
# n = int(input())
# lose = list(map(int,input().split()))
# happy = list(map(int,input().split()))

# # dp[i][j] = 체력이 j일때, 처음 i명을 통해 가질 수 있는 최대 행복
# dp = [[0] * 101 for _ in range(n+1)]

# for i in range(1,n+1):
#     for j in range(100):
#         if j >= lose[i-1]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-lose[i-1]] + happy[i-1])
#         else:
#             dp[i][j] = dp[i-1][j]

# print(dp[n][99])


# 사람의 수 n
n = int(input())
lose = ['dummy'] + list(map(int,input().split()))
happy = ['dummy'] + list(map(int,input().split()))

# dp[i][j] = 체력이 j일때, 처음 i명을 통해 가질 수 있는 최대 행복
dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if j >= lose[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lose[i]] + happy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])


