# 이중우선순위큐
# 힙
# https://programmers.co.kr/learn/courses/30/lessons/42628

from bisect import bisect_left


def solution(operations):
    answer = []
    print('----------------------')

    for row in operations:
        opr, num = row.rsplit()
        if opr == 'I':
            index = bisect_left(answer, int(num))
            answer.insert(index, int(num))
        else:
            if answer:
                if num == '1':
                    del answer[-1]
                else:
                    del answer[0]
        print(answer)

    if answer:
        return [answer[-1], answer[0]]
    else:
        return [0, 0]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
