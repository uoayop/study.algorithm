# 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque

def solution(s):
    def test(lst):
        stack = []
        sleft, mleft, lleft = 0, 0, 0
        for c in lst:
            if (sleft<0 or mleft<0 or lleft<0):
                return False
            if c=='(': sleft += 1
            elif c=='{' : mleft += 1
            elif c=='[' : lleft += 1
            elif c== ')' : sleft -= 1
            elif c== '}' : mleft -= 1
            elif c== ']' : lleft -= 1
            print(c, sleft,mleft, lleft)
        if sleft==0 and mleft==0 and lleft==0:
            return True
        return False
                
    s = list(s)
    q = deque(s)
    answer = 0
    for i in range(len(s)):
        print(q)
        # 시작이 여는 괄호면 올바른 괄호 문자열이 아니므로 continue
        if q[0]==')' or q[0]=='}' or q[0]==']':
            q.append(q.popleft())
            continue
        else:
            # 올바른 괄호 문자열이면 true 반환
            if (test(q)):
                answer += 1
        # 왼쪽으로 회전
        q.append(q.popleft())
        
    return answer

print(solution("[](){}"))