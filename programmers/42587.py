#프린터

def solution(priorities, location):
    answer = 0

    while (priorities):
        highest_p=max(priorities)       #리스트에서 가장 높은 우선순위 저장
        temp = priorities.pop(0)        #제일 앞에 있는 문서 pop
        
        if (temp < highest_p):      #현재 문서가 가장 높은 우선순위가 아니면
            priorities.append(temp)     #대기 목록 마지막에 다시 삽입
            
            if location==0: #몇번째로 출력되는지 알고싶은 문서의 위치가 첫번째였다면
                location = len(priorities)-1    #대기 목록의 마지막으로 보냈으니까 위치 다시 조정해줌
            else:
                # 첫번째가 아니였다면 한칸씩 앞으로 땡겨졌으니까 인덱스에서 1 빼줌
                location -= 1

        
        else:   #현재 문서가 가장 높은 우선 순위라면 
            answer+=1   #출력 횟수 +1
            if location==0:     # 우리가 찾던 문서가 출력 됐으니까 break
                break
            else:
                location-=1     # 우리가 찾던 문서가 아니니까 인덱스에서 1 빼줌

    return answer

    




print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))