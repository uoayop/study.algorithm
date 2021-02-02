#08.빗물트래핑

# def trapping_rain(buildings):
#
#     # 빗물 초기값 정의
#     rain = 0
#
#     #처음부터 끝까지
#     for i in range(len(buildings)):
#         # 맨 앞과 끝에는 빗물이 들어갈 수 없다.
#         if i == 0 or i == len(buildings) - 1:
#             continue
#
#         # 왼쪽, 오른쪽 가장 높은 빌딩 값 찾기
#         left_high = max(buildings[:i])
#         right_high = max(buildings[i + 1:])
#
#         # 더 낮은 빌딩을 기준 높이로 지정
#         std_high = min(left_high, right_high)
#
#         # 빗물 값 계산
#         if left_high > buildings[i] and right_high > buildings[i]: # 왼쪽,오른쪽 둘다 높을 때
#             temp_rain = std_high - buildings[i]
#             rain += temp_rain
#
#     return rain


def trapping_rain(buildings):

    stack=[]
    rain=0

    for i in range(len(buildings)):
        #현재 높이가 이전 높이보다 높을 때
        while stack and buildings[i]>buildings[stack[-1]]:

            print("stack=",stack)
            print("building[i]=%d,bildings[stack[-1]]=%d"%(buildings[i], buildings[stack[-1]]))
            #스택에서 꺼냄
            top=stack.pop()

            #스택이 비어있으면 break
            if not len(stack):
                break

            #칸 사이의 거리 구하기
            distance = i - stack[-1] - 1

            #가장 낮은 높이의 블록높이만큼 쌓인 물 구하기
            temp_water=min(buildings[i], buildings[stack[-1]]) - buildings[top]

            #Q. building[i],bilding[stack[-1]],building[top] 세개 차이?
            rain += distance * temp_water

        #스택이 비어있거나 현재 높이가 더 낮으면 스택에 인덱스를 넣음
        stack.append(i)

    return rain


print(trapping_rain([0,1,0,2,1,0,1,3,2,1,2,1]))

