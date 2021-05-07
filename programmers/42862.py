# 체육복
#https://programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    student = [1 for _ in range(n)]

    s_reserve = list(set(reserve)-set(lost))
    s_lost = list(set(lost)-set(reserve))

    print(s_lost, s_reserve)
    for l in s_lost:
        # 옷을 도난당한 학생의 오른쪽 학생이 여분이 있다면
        # 여분있는 학생 목록에서 오른쪽 학생을 지움
        if l-1 in s_reserve:
            s_reserve.remove(l-1)
        elif l+1 in s_reserve:
            s_reserve.remove(l+1)
        # 옷을 도난당한 학생의 왼쪽 학생이 여분이 있다면
        # 여분있는 학생 목록에서 왼쪽 학생을 지움
        # 양쪽 학생이 모두 여분이 없다면 
        # 체육 수업을 들을 수 없기때문에 전체 학생 수에서 1을 빼줌
        else:
            n -= 1

    return n


print(solution(5, [2, 4], [1, 4, 5]))
