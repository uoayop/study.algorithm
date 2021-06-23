# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883
# 탐욕법, 그리디

def solution(number, k):
    stack = []

    # 스택 가장 위에 있는 숫자 < 넣으려는 숫자인 경우
    # 스택에 있는 수를 모두 비교해주면서 뺴준다.
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    # 만약 k가 남을 경우, 뒤에서부터 숫자를 제거해준다.
    while k > 0:
        stack.pop()
        k -= 1

    return "".join(stack)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))


print(solution("87654321", 3))
# # 오답
# def solution(number, k):
#     answer = ''
#     dcnt = 0
#     number = list(map(int, number))
#     largest, smallest = -1, 1000001

#     def maxCheck(index):
#         if largest < number[index]:
#             return 1
#         return 0

#     def minCheck(index):
#         if largest != number[index] and smallest >= number[index]:
#             return 1
#         return 0

#     for index, curr in enumerate(list(number)):
#         if maxCheck(index) and len(number)-(index + 1)-dcnt > 0:
#             largest = curr
#             dcnt += len(answer)
#             answer = '' + str(curr)
#             smallest = curr
#         else:
#             if minCheck(index):
#                 dcnt += 1
#                 smallest = curr
#             else:
#                 answer += str(curr)
#         if dcnt == k:
#             for i in range(index+1, len(number)):
#                 answer += str(number[i])
#             break

#     return answer


# 오답 : 84321, 정답: 87654
# 테스트케이스 : https://programmers.co.kr/questions/13043
