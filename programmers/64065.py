# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = list(s.split("}"))
    del s[-1], s[-1]

    for i in range(len(s)):
        s[i] = s[i].replace(",{","").replace("{","")
        
    dct = {}
    for row in s:
        nums = row.split(",")
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1

    answer = sorted(list(dct.items()), key = lambda x: x[1], reverse = True)
    ans = []
    for a in answer:
        ans.append(int(a[0]))

    return ans

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))