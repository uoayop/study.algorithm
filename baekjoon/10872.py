# 10872 팩토리얼
#https://yeol2.tistory.com/38

import sys

def makestar(n):
    result=[]
    legnth=len(n)
    for i in range(3*legnth):
        if i//legnth==1: #몫이 1일 경우
            result.append(n[i%legnth] + " " * legnth + n[i%legnth])
        else:
            result.append(n[i%legnth]*3)
    return (list(result))

n=int(sys.stdin.readline())
star=["***","* *","***"]

k=0
while n!=3:
    n=int(n/3)
    k+=1

for i in range(k):
    star=makestar(star)
for i in star:
    print(i)