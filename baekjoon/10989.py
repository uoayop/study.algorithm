#수 정렬하기3
#수 범위가 작으면 카운팅 정렬로 정렬 가능

import sys

array=[]
for i in range(0,10001):
    array.append(0)

num=int(sys.stdin.readline().rstrip())

for i in range(num):
    temp=int(sys.stdin.readline())
    array[temp]+=1

for i in range(0,10001):
    for j in range(0,array[i]):
        print(i)