#방 번호
#시뮬레이션
#https://www.acmicpc.net/problem/1475

import sys
input = sys.stdin.readline

n = input().rstrip()
check = [0] * 10

for i in range(len(n)):
    check[int(n[i])]+=1

sum = check[6] + check[9]
# 더한 값이 홀수이면 세트 +1
if sum % 2 == 1:
    sum += 1

check[6] = sum//2
check[9] = sum//2
print(max(check))