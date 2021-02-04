#단어 변환
#https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

import sys
MAX_INT = 52372727
def compare(s1,s2):
    #다르면 False
    cnt = 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            cnt+=1
            if cnt==2 : return False
    return True

def solution(begin, target, words):
    visited = [0] * len(words)
    if target not in words : return 0

    def dfs(depth,word):
        if word == target: return depth

        ret = MAX_INT
        for i,w in enumerate(words):
            #현재 단어랑 알파벳이 한개만 차이 나면
            if compare(word,w) and visited[i]==0:
                visited[i]=1 #그 단어 방문해줘
                ret = min(ret, dfs(depth+1, w))
                visited[i]=0 #방문 해제를 무조건 해줘야 한다. 왜냐면 다른 단어가 그 경로로 다시 들어갈 수도 잇잖아
                # A -> B -> C  -> D 였는데 C에서 B로 돌아와서 D로 갈 수 없어
        return ret
        

    ret = dfs(0,begin)

    if ret == MAX_INT:
        return 0
    else:
        return ret

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
