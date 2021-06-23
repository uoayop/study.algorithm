# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

import sys
from collections import deque

def solution(s):
    if len(s) == 1:
        return 1

    answer = sys.maxsize

    def check(split):
        stack = deque()
        cnt = 1
        for i in range(0, len(s), split):
            curr = s[i : i + split]
            if stack:
                if stack[-1][0] == curr:
                    cnt += 1
                    stack.pop()
                else:
                    cnt = 1
            stack.append([s[i : i + split], cnt])

        # print(stack)
        ret = 0
        while stack:
            char, leng = stack.popleft()
            ret += (len(char) + len(str(leng))) if leng > 1 else (len(char))
            
        return ret

    for split in range(len(s) // 2, 0, -1):
        # print(split)
        answer = min(answer, check(split))

    return answer

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
# print(solution("aabaab"))
# print(solution("acacacbacacac")) 
print(solution("acacacacacacbacacacacacac"))
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
# 100a