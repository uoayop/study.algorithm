#수찾기
#https://www.acmicpc.net/problem/1920

import sys

def solution(list_n, list_m):
    check = {}
    
    for num in list_n: #list_n의 숫자들 저장
        check[num] = 1
            
    for num in list_m:
        if num not in check:
            print("0")
        else:
            print("1")

n=int(sys.stdin.readline().rstrip())
list_n = list(map(int,sys.stdin.readline().rstrip().rsplit()))
m=int(sys.stdin.readline().rstrip())
list_m = list(map(int,sys.stdin.readline().rstrip().rsplit()))

solution(list_n,list_m)