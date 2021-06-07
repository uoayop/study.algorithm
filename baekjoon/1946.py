# 신입사원
# 그리디
# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    humans = sorted([list(map(int,input().rsplit())) for _ in range(n)])

    print(humans)

    compare = humans[0][1]
    cnt = 0
    for i in range(1,n):
        target = humans[i][1]
        compare = min(compare, target)
        if compare < target:
            cnt += 1
    
    print(">>",n-cnt)

# sorted([list(map(int,input().rsplit())) for _ in range(n)], key = lambda x: (x[1],x[0]))

# n = 7
# humans = [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]

