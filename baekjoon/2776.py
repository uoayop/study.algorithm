# 암기왕
# https://www.acmicpc.net/problem/2776
# 이분탐색


'''
이분탐색
'''
# import sys
# input = sys.stdin.readline
# 하루동안 본 정수 수첩 1
# 봤다고 주장하는수 수첩 2
# 수첩 2의 숫자가 수첩 1에 있으면 1, 없으면 0 출력

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     note1 = sorted(list(map(int,input().rsplit())))
#     m = int(input())
#     note2 = list(map(int,input().rsplit()))


#     for note in note2:
#         l , r = 0, n-1
#         flag = False
#         while l <= r:
#             mid = (l + r) // 2
#             if note1[mid] > note:
#                 r = mid - 1
#             elif note1[mid] < note:
#                 l = mid + 1
#             else:
#                 flag = True
#                 break
#         if flag:
#             print(1)
#         else:
#             print(0)

'''
defaultdict
'''
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     note1 = sorted(list(map(int,input().rsplit())))
    
#     check = defaultdict(int)
#     for temp in note1:
#         check[temp] += 1

#     m = int(input())
#     note2 = list(map(int,input().rsplit()))

#     for note in note2:
#         if note in check:
#             print(1)
#         else:
#             print(0)

'''
카운터
'''
import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    note1 = list(map(int,input().rsplit()))
    
    check = Counter(note1)

    m = int(input())
    note2 = list(map(int,input().rsplit()))

    for note in note2:
        if note in check:
            print(1)
        else:
            print(0)