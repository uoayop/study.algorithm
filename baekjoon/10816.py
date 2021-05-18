#숫자카드2
#https://www.acmicpc.net/problem/10816


# 딕셔너리 사용
# import sys

# def solution(list_n, list_m):
#     check = {}
#     result = []
#     for num in list_n: #list_n의 숫자들 저장
#         if num not in check:
#             check[num] = 1
#         else:
#             check[num]+=1
            
#     for num in list_m:
#         if num not in check:
#             result.append(0)
#         else:
#             result.append(check[num])
#     return result

# #상근이가 갖고 있는 카드의 수 n, 상근이 숫자 카드 card_n
# n=int(sys.stdin.readline().rstrip())
# card_n = list(map(int,sys.stdin.readline().rstrip().rsplit()))

# #구해야 할 카드의 수 m, 카드의 숫자 card_m
# m=int(sys.stdin.readline().rstrip())
# card_m = list(map(int,sys.stdin.readline().rstrip().rsplit()))

# print(*(solution(card_n,card_m)))



# 이진 탐색

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().rsplit()))
cards_cnt = defaultdict(int)

for c in cards:
    cards_cnt[c] += 1

m = int(input())
check = list(map(int,input().rsplit()))

for c in check:
    l, r = 0, len(cards)
    while l <= r:
        mid = (l + r) // 2
        if mid < c:
            l = mid + 1
        elif mid > c:
            r = mid - 1
        else:
            break
    
    print(cards_cnt[c], end=' ')
print()