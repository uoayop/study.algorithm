# 나무 자르기
# https://www.acmicpc.net/problem/2805
# 이진 탐색

import sys
input = sys.stdin.readline

# 나무 m미터가 필요, 절단기 높이 h
# 높이가 h보다 큰 나무들이 잘림

# 나무의 수 n, 필요한 나무 m
n, m = map(int, input().rsplit())
trees = list(map(int, input().rsplit()))

l, r = 0, max(trees)
check = 0

while l <= r:
    h = (l + r) // 2
    total = sum(t-h if h < t else 0 for t in trees)
    # print("total:{0}, h:{1}, l:{2}, r:{3}".format(total, h, l, r))
    if total >= m:
        check = max(check, h)
        l = h + 1
    else:
        r = h - 1

print(check)

# l = 0
# r = max(trees)
# check = 0
# total = sys.maxsize

# while total > m:
#     h = (l + r) // 2

#     total = sum(t-h if h < t else 0 for t in trees)
#     print("total:{0}, h:{1}, l:{2}, r:{3}".format(total, h, l, r))

#     if total < m:
#         l = h + 1
#         check = h
#     elif total == m:
#         print(h)
#         break
#     elif total > m:
#         # l += 1
#         l = h 

# print(check)

'''
input:
5 2000000000
900000000 900000000 900000000 900000000 900000000

output:
500000000
-
input:
5 200
90 90 90 90 90   
output:
50

total:225, h:45, l:0, r:90
total:110, h:68, l:46, r:90
total:170, h:56, l:46, r:67
total:200, h:50, l:46, r:55
total:185, h:53, l:51, r:55
total:195, h:51, l:51, r:52
'''
