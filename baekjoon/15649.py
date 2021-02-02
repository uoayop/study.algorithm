#n과 m 1
#1부터 n까지 자연수 중에서 중복없이 m개를 고른 수열
#백트래킹은 이미 지나쳐온 곳을 다시 돌아가서 다른 가능성을 시도해보는 걸
#반복하는 기법. 

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
        if check_list[i]==1: #이전에 출력된 숫자이면 무시
            continue
        result_list[index]=i #해당 인덱스에 숫자 넣어줌
        check_list[i]=1      #출력된 숫자 체크

        check(index+1,n,m)   #다음숫자 출력
        check_list[i]=0      #초기화

check(0,n,m)