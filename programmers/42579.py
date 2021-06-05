# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579
# 해시

from collections import defaultdict

def solution(genres, plays):
    s_genre = defaultdict(list)
    s_play = defaultdict(int)

    for i in range(len(genres)):
        s_genre[genres[i]].append((i,plays[i]))
        s_play[genres[i]] += plays[i]

    # print(s_genre)
    # print(s_play)

    s_play = sorted(s_play.items(), key = lambda x: x[1], reverse = True)

    answer = []
    for play in s_play:
        gen = play[0]
        i = 0
        for temp in sorted(s_genre[gen], key = lambda x: x[1], reverse = True):
            answer.append(temp[0])
            i += 1
            if i == 2:
                break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))