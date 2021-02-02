#완주하지 못한 선수

def solution(participant, completion):
    freqs = {}
    answer = ''
    
    for p_man in participant: #참여자 명단 빈도수 저장
        if p_man not in freqs:
            freqs[p_man] = 1
        else:
            freqs[p_man] += 1
            
    for c_man in completion:  #완주자를 참여자 명단의 빈도수에서 1씩 빼줌, 명단에 없으면 출력
        freqs[c_man] -= 1
        
    for result in freqs:
        if freqs[result]==1:
            answer+=result

    return answer

print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))