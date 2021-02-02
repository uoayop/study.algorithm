#카드2
#https://www.acmicpc.net/problem/2164

import sys
import collections

card = collections.deque()

n=int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    card.append(i)

while (len(card)!=1):
    card.popleft()
    card.append(card.popleft())

print(card.pop())