#퇴사
#https://www.acmicpc.net/problem/14501
#DP

# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input().rstrip())
# meets = [['dummy']]

# for _ in range(n):
#     meets.append(list(map(int,input().rstrip().rsplit())))
    
# max_pays = 0

# for index in range(1,n+1):
#     q = deque()
#     q.append((index,0))
#     print('---------------')
#     while q:
#         i,cnt = q.popleft()
#         print(i,cnt)
#         if i +  meets[i][0] <= n:
#             cnt += meets[i][1]
#             q.append((i + meets[i][0], cnt))
#         elif i+ meets[i][0] == n:
#             max_pays = max(max_pays, cnt)
       

# print(max_pays)


import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
meets = []

for _ in range(n):
    meets.append(list(map(int,input().rstrip().rsplit())))
    
memo = [0 for _ in range(n+1)]
max_pay = 0

for i in range(n):
    day, pay = meets[i][0], meets[i][1]
    # 이전에 저장된 값과 memo[i] 중 더 큰것으로 갱신
    max_pay = max(max_pay, memo[i])

    if i+day > n:
        continue
    # 현재까지의 수익 + 이번 상담 수익 vs 오늘 상담이 끝나는 시점의 수익
    # 더 큰 값을 비교해준다
    # 일을 할수도 있고 안할수도 있기 떄문이다.
    memo[i+day] = max(max_pay+pay, memo[i+day])

print(max(memo))
    
#https://dndi117.tistory.com/entry/aaa


# for i in range(n,0,-1):
#     next_index = i + meets[i][0]
#     if i==n:
#         if meets[i][0] == 1:
#             pays[i] = meets[i][1]
#     elif next_index == n+1:
#         pays[i] = max(meets[i][1], pays[i+1])
#     elif next_index < n+1:
#         pays[i] = max(meets[i][1] + pays[next_index], pays[i+1])
#     else:
#         pays[i] = pays[i+1]

# print(pays[1])

# for index in range(1,n+1):
#     q = deque()
#     q.append((index,0))
#     print('---------------')
#     while q:
#         i,cnt = q.popleft()
#         print(i,cnt)
#         if i +  meets[i][0] <= n:
#             cnt += meets[i][1]
#             q.append((i + meets[i][0], cnt))
#         elif i+ meets[i][0] == n:
#             max_pays = max(max_pays, cnt)
       

# print(max_pays)