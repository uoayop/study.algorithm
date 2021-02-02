#2798 블랙잭

import sys

order= sys.stdin.readline().rstrip().split()
n=int(order[0])
goal=int(order[1])
result=0

num = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            hap=num[i]+num[j]+num[k]
            if result< hap <= goal:
                result = hap

print(result)