# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for c in s:
        if (not stack):
            stack.append(c)
            
        else:
            if (stack[-1] == c):
                stack.pop()
            else:
                stack.append(c)
                
    if (stack):
        return 0
    return 1


print(solution("baabaa"))
print(solution("cdcd"))
