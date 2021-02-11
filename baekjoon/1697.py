#숨바꼭질
#bfs
#https://www.acmicpc.net/problem/1697

import sys
from collections import deque
input = sys.stdin.readline

MIN_NUM = 100003
n, k = map(int,input().rstrip().rsplit())
location, sec = [n-1, n+1, 2 * n] , 1
visit = {}

queue = deque()
for l in location:
    queue.append([l,sec])

if n==k:
    print(0)
    sys.exit()

while(queue):
    num, sec = queue.popleft()

    if 0 <= num and num < 100003 and visit.get(num) is None:
        if num == k:
            MIN_NUM = min(sec,MIN_NUM)
        else:
            visit[num] = 1
            if 0 <= num-1 < 100003:
                if visit.get(num-1) is None:
                    queue.append([num-1,sec+1])
            if 0 <= num+1 < 100003:
                if visit.get(num+1) is None:
                    queue.append([num+1,sec+1])
            if 0 <= num*2 < 100003:
                if visit.get(num*2) is None:
                    queue.append([num*2,sec+1])

print(MIN_NUM)