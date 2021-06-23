# 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    
    def check(num):
        cnt = 0
        for i in range(1,num+1):
            if num % i ==0:
                cnt += 1
        if cnt % 2 == 0:
            return True
        return False
    
    for i in range(left, right+1):
        if check(i):
            answer += i
        else:
            answer -= i
    
    return answer