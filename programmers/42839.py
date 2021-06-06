# 소수 찾기
# 완전 탐색
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
from collections import defaultdict


def solution(numbers):
    nums = list(numbers)
    answer_lst = defaultdict(int)

    def check(num):
        if num < 2:
            return False
        if num == 2:
            return True

        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True

    answer = 0
    for i in range(1, len(nums)+1):
        lst = list(permutations(nums, i))
        # print(lst)
        for row in lst:
            temp = ''
            for char in row:
                temp += char
            if answer_lst[int(temp)] == 0 and check(int(temp)):
                print(int(temp))
                answer_lst[int(temp)] = 1
                answer += 1

    return answer


print(">>",solution("17"))
print(">>",solution("011"))
print(">>",solution("235"))
print(">>",solution("111"))

'''
[('0',), ('1',), ('1',)]
[('0', '1'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '0'), ('1', '1')]
[('0', '1', '1'), ('0', '1', '1'), ('1', '0', '1'), ('1', '1', '0'), ('1', '0', '1'), ('1', '1', '0')]
'''
