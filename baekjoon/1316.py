#그룹단어체크
#https://www.acmicpc.net/problem/1316

#첫째 줄 단어 개수 N, 둘째 줄 단어

import sys

n=int(sys.stdin.readline())
check_cnt=0

for i in range(n):
    string_check=[]
    back_str=""
    string=sys.stdin.readline().rstrip()

    for i in range(0,len(string)):
        if (back_str==string[i]):
            string_check.append(string[i])

        elif (string[i] not in string_check):
            string_check.append(string[i])

        back_str=string[i]

    if (len(string_check)==len(string)):
        check_cnt+=1

print(check_cnt)


