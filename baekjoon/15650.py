#n과 m 2

import sys

n,m= map(int, sys.stdin.readline().rstrip().split())
check_list=[0]*(n+1)
result_list=[0]*(m)

def check(index,n,m):
    if index==m:
        for i in range(m):
            print(result_list[i],end=" ")
        print()
        return

    for i in range(1,n+1):
        #이전에 출력된 숫자이면 무시
        if (check_list[i]==1): 
            continue
        result_list[index]=i #해당 인덱스에 숫자 넣어줌
        for j in range(i+1):
            check_list[j]=1  #출력된 숫자보다 작은 숫자 체크

        check(index+1,n,m)   #다음숫자 출력

        for j in range(1,n+1):
            check_list[j]=0      #초기화

check(0,n,m)