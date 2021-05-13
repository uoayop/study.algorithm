#평범한 배낭
#https://www.acmicpc.net/problem/12865
#dp

# import sys
# input = sys.stdin.readline

# # -------틀렸고
# n,k = map(int,input().rstrip().rsplit())
# bag = ['dummy']
# dp = ['dummy']

# for _ in range(n):
#     row = tuple(map(int,input().rstrip().rsplit()))
#     bag.append(row)
#     dp.append(row[1])

# max_num = 0
# for i in range(1,n+1):
#     for j in range(1,i):
#         # 두 물건의 무게가 k보다 작거나 같을 때
#         if bag[i][0] + bag[j][0] <= k:
#             print("[i = {}, j = {}]".format(i,j))
#             print("max(dp[{}] +bag[{}][1] = {}, dp[{}] ={}".format(j,i,dp[j]+bag[i][1],j,dp[j]))
#             dp[i] = max(bag[j][1] + bag[i][1],
#                         dp[j])
#         if dp[i] > max_num:
#             max_num = dp[i]

# print(max_num)


import sys
input = sys.stdin.readline

#https://suri78.tistory.com/2

n,k = map(int,input().rstrip().rsplit())
bag = ['dummy']

# dp[i][j] = 물건 무게의 합이 j일때, 처음 i개의 아이템 중 담을 수 있는 최대 가치
# ( j = 1 ~ k )

# j가 현재 물건의 무게 w보다 작을때 : w를 담을 수 없으므로 전의 값을 복사한다.
# dp[i][j] = dp[i-1][j]

# j가 현재 물건의 무게 w와 같거나 클 때 : 물건을 담았을 때와 담지 않았을 때 max 값을 찾아준다.
# dp[i][j] = max( dp[i-1][j] , dp[i-1][j-w] + v)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    row = tuple(map(int,input().rstrip().rsplit()))
    bag.append(row)

for i in range(1,n+1):
    for j in range(1, k+1):
        # 현재 물건의 무게 w, 현재 물건의 가치 v
        w = bag[i][0] 
        v = bag[i][1]

        # 물건을 담을 수 있을 때
        if j >= w:
            # (현재 물건을 담지 않았을 때 갖는 최댓값 vs 현재 물건을 담았을 때 갖는 최댓값)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])



# dp = ['dummy']

# for _ in range(n):
#     row = tuple(map(int,input().rstrip().rsplit()))
#     bag.append(row)
#     dp.append(row[1])

# max_num = 0
# for i in range(1,n+1):
#     for j in range(1,i):
#         # 두 물건의 무게가 k보다 작거나 같을 때
#         if bag[i][0] + bag[j][0] <= k:
#             # print("[i = {}, j = {}]".format(i,j))
#             # print("max(dp[{}] +bag[{}][1] = {}, dp[{}] ={}".format(j,i,dp[j]+bag[i][1],j,dp[j]))
#             dp[i] = max(bag[j][1] + bag[i][1],
#                         dp[j])
#         if dp[i] > max_num:
#             max_num = dp[i]

# print(max_num)
