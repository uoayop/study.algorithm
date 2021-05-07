# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

# def solution(numbers):
#     answer = ''
#     numbers = list(map(str, numbers))
#     numbers = (sorted(numbers, key=lambda x: (x[0], x[-1]), reverse=True))
#     print(numbers)
#     for n in numbers:
#         answer += str(n)
#     return answer

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = (sorted(numbers, key=lambda x: x * 5, reverse=True))

    for n in numbers:
        answer += str(n)
    return str(int(answer))

print(solution([3, 30, 34, 5, 9]))

print(solution([40,403]))

print(solution([4223,4991]))
#[3, 30, 34, 5, 9]

#[우선순위]
# 1. 자릿수가 작고, 숫자가 클 수록
# 2. 자릿수가 크고, 숫자가 클 수록
#  - 자릿수가 같다면 뒷자리 숫자가 클 수록
# 3. 자릿수가 작고, 숫자가 작을수록
# 4. 자릿수가 작고, 숫자가 작을수록