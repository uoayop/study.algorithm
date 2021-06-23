# 조이스틱
# 그리디
# https://programmers.co.kr/learn/courses/30/lessons/42860


# ????????
# https://blog.naver.com/jaeyoon_95/221740770765
'''
좌우로 움직이는 것은 'A'를 만나면 알파벳을 바꾸지 않아도 되므로 오른쪽에 'A'가 아닌 곳에
 더 빨리 만나는 쪽을 찾으면 됩니다! 
 따라서 반복문을 사용해서 왼쪽, 오른쪽으로 갈 경우 'A'가 아닌 문자가 언제 나오는지를 찾고, 
 더 작은 값을 사용하였습니다.
[출처] [프로그래머스] 조이스틱|작성자 재윤
'''
def solution(name):
    name = list(name)
    answer = 0
    curr = 0

    while 1:
        left, right = 1, 1
        if name[curr] != 'A':
            left = 1
            right = 1
            UpDown = min((ord('Z') - ord(name[curr])) + 1, ord(name[curr]) - ord('A'))
            answer += UpDown
        name[curr] = 'A'
        if name == ['A'] * len(name): break
        for i in range(1,len(name)):
            if name[curr + i]=='A':
                right += 1
            else: break
        for i in range(1, len(name)):
            if name[curr - i] == 'A':
                left += 1
            else: break
        if right > left:
            answer += left
            curr -= left
        else:
            answer += right
            curr += right

    return answer

print(solution("JAN")) 
print(solution("JEROEN"))


'''
def solution(name):
    answer = 0
    name=list(name)
    index=0
    while(True):
        right=1
        left=1
        if name[index] != 'A': 
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1))
            answer += updown
        name[index] = 'A'
        if name == ["A"]*len(name): break
        for i in range(1,len(name)):
            if name[index+i]=="A": right+=1
            else: break
        for i in range(1,len(name)):
            if name[index-i]=="A": left+=1
            else: break
        if right>left:
            answer+=left
            index-=left
        else:
            answer+=right
            index+=right
    return answer


'''