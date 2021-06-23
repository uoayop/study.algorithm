# 구명 보트
# 탐욕법, 그리디

def solution(people, limit):
    answer = 0
    people.sort()
    l, r = 0, len(people)-1

    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
            answer += 1
        else:
            r -= 1
            answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([10,20,30,40,70,100], 100))