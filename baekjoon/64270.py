# 덩치
# https://www.acmicpc.net/problem/64270

import sys
input = sys.stdin.readline

n = int(input())
student = []

for _ in range(n):
    student.append(list(map(int,input().rsplit())))

# s[0] = weight, s[1] = height
for s1 in student:
    rank = 1
    for s2 in student:
        # 키와 덩치가 모두 큰 학생의 수 만큼 순위가 떨어짐
        if s1[0] < s2[0] and s1[1] < s2[1]:
            rank += 1

    print(rank,end=' ')
print()