#통계학

import sys
from collections import Counter

def avg(arr):
    sum=0
    for i in arr:
        sum+=i
    return round((sum/len(arr)))

def mid(arr):
    arr=sorted(arr)
    mid=len(arr)//2
    return (arr[mid])

def freq(arr):
    if (len(arr)==1):
        return arr[0]
    arr=sorted(arr)
    c=Counter(arr)
    first=c.most_common(1)
    second=c.most_common(2)
    if (first[0][1]==second[1][1]): return second[1][0]
    return first[0][0]

def ran(arr):
    return(max(arr)-min(arr))


n=int(sys.stdin.readline())
num=[]

for i in range(n):
    temp=int(sys.stdin.readline().rstrip())
    num.append(temp)

print(avg(num))
print(mid(num))
print(freq(num))
print(ran(num))