#기능 개발

def solution(progresses, speeds):
    answer = []
    count = 0
    full_progresses=0
    len_max = len(progresses)
    
    #개발 완료된 기능의 수가 progresses의 수와 같아지면 break
    while(count!=len_max):
        #가장 앞에 있는 기능의 진도가 100보다 커지면 break
        while(progresses[0]<100):
            for i in range(len(progresses)):
                #각각의 기능에 맞는 속도로 진도를 나감
                progresses[i] += speeds[i]

        while (progresses):
            #현재 가장 앞에 있는 기능의 진도와 해당 기능 개발속도 pop
            temp = progresses.pop(0)
            temp_speed = speeds.pop(0)
            if (temp>=100):
                #만약 진도가 100 이상이면 배포할수 있으므로 full_progresses+=1
                full_progresses+=1
            else:
                #진도가 100이 안되므로 pop했던 개발 진도, 속도 다시 삽입
                progresses.insert(0,temp)
                speeds.insert(0,temp_speed)
                #다음날로 넘어가기
                break

        #answer 리스트에 full_progresses 삽입하기
        answer.append(full_progresses)

        #count 변수로 개발 완료된 기능의 수 세기
        count+=full_progresses

        #full_progresses 초기화
        full_progresses=0

    return answer

# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

print(solution([96, 99, 98, 97], [1, 1, 1, 1]))
print(solution([1, 3, 0, 2], [1, 1, 1, 1]))
print(solution([99, 1, 99, 1] ,[1, 1, 1, 1]))
print(solution([40, 93, 30, 55, 60, 65],[60, 1, 30, 5 , 10, 7]))