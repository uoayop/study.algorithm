# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re


def solution(expression):
    answer = -1
    expression = re.split(r'(\D)', expression)
    '''
    \D 십진 숫자가 아닌 모든 문자와 일치합니다. 이것은 \d의 반대입니다. ASCII 플래그를 사용하면 [^0-9]와 동등합니다.
    = 숫자가 아닌 문자와 매칭됨
    '''

    def check(expresses):
        lst = expression[:]
        for express in expresses:
            index = 0
            while express in lst:
                check = lst[index]
                if check == express:
                    result = cal(check, lst[index-1], lst[index+1])
                    lst.insert(index-1, result)
                    for i in range(3):
                        del lst[index]
                else:
                    index += 1
                    index %= len(lst)
        return abs(lst[0])

    def cal(express, num1, num2):
        num1, num2 = int(num1), int(num2)
        if express == '+':
            return num1 + num2
        elif express == '-':
            return num1 - num2
        elif express == '*':
            return num1 * num2

    answer = max(check(['+', '-', '*']), check(['+', '*', '-']), check(['-', '+', '*']),
                    check(['-', '*', '+']), check(['*', '+', '-']), check(['*', '-', '+']))

    return answer


# print(solution("1-2*3-5+2"))
# print(solution("50*6-3*2"))
# print(solution("100-200*300-500+20"))
# print(solution("200-300-500-600*40+500+500"))
# print(solution("2*2*2*2*2-2*2*2"))
print(solution("2-990-5+2"))