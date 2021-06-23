# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

from  collections import defaultdict

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    common, union = 0, 0

    dct1, dct2 = defaultdict(int), defaultdict(int)

    def dictionary(dct, str):
        for i in range(0, len(str)-1):
            curr = str[i : i + 2]
            if curr.isalpha():
                dct[str[i : i+2]] += 1

    def checkCommon():
        cnt = 0
        for s in dct1:
            if dct2[s] > 0:
                cnt += min(dct1[s], dct2[s])
        return cnt

    def checkUnion(s1, s2):
        cnt = 0
        for s in s1:
            if s2[s] > 0:
                cnt += max(dct1[s], s2[s])
                s2[s] = 0
            else:
                cnt += s1[s]
            s1[s] = 0
        return cnt

    dictionary(dct1, str1)
    dictionary(dct2, str2)

    # print(dct1)
    # print(dct2)

    common = checkCommon()
    union += checkUnion(dct1, dct2)
    union += checkUnion(dct2, dct1)

    # print(common, union)
    
    # or 이 아니고 and임! 왜냐면 합집합, 교집합이 """모두""" 0일때만 1로 취급하기 때문!
    # https://programmers.co.kr/questions/13954
    
    if common == 0 and union == 0:
        return 65536
    answer = int(common / union * 65536)
    return answer


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))