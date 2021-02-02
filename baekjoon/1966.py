#프린터 큐
#https://www.acmicpc.net/problem/1966

import sys
import collections


#테스트 케이스 수 t
#문서의 개수 n, 궁금한 문서의 인덱스 위치 m
#n개의 문서의 중요도 리스트 p_list

t=int(sys.stdin.readline().rstrip())
for i in range(t):
    printer=collections.deque()
    n,m = map(int,sys.stdin.readline().rsplit())
    p_list = list(map(int,sys.stdin.readline().rsplit()))
    count = 0

    if n==1: 
        print(1)
        continue

    for p in p_list:
        printer.append(p)
    
    while(printer):
        max_num = max(printer)
        check_doc=printer.popleft()

        #맨 앞의 요소가 가장 큰 값일 때
        if (check_doc==max_num):
            count+=1
            #근데 그 요소가 우리가 궁금한 요소이면
            if (m==0):
                print(count)
                break
            #우리가 원하는 요소가 아니면
            else:
                m -= 1
            
        
        #맨 앞 요소가 가장 큰 값이 아니면
        else:
            #가장 맨 뒤에 삽입
            printer.append(check_doc)
            #근데 그 요소가 우리가 궁금한 요소이면 맨 뒤로 바꿔줌
            if (m==0):
                m = len(printer)-1
            # 그 요소가 우리가 궁금해 하는 요소가 아니니까 한칸 앞으로 땡겨줌
            else:
                m -= 1
            

        
            
