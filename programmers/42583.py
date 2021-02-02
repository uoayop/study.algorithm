# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     ing_truck = deque()
#     ing_weight = 0
#     truck_count = len(truck_weights)
#     count = 0
    
#     while 1:
#         if (count == truck_count):
#             break

#         if (truck_count==1):
#             return bridge_length+1
            
#         #트럭 하나 꺼냄
#         if (truck_weights):
#             truck = truck_weights.pop(0)
#             ing_truck.append(truck)
#             ing_weight += truck
#         #print('[다리 건너기 전] {0}:{1} / {2}:{3}\n'.format("ing_truck",ing_truck,"ing_weight",ing_weight))
        
#         #다리를 건너는 동안
#         for i in range(bridge_length): 
#             #만약 건너고 있는 트럭의 무게가 한계보다 가벼우면 트럭 하나 더 꺼냄
#             if (ing_weight <= weight and truck_weights):
#                 truck = truck_weights.pop(0)
#                 ing_truck.append(truck)
#                 ing_weight += truck
            
#             if (ing_weight > weight):
#                 ing_truck.pop()
#                 ing_weight -= truck
#                 truck_weights.insert(0,truck)
#                 #print('[ing_weight가 더 크면] {2} - {0}:{1} / {3}:{4}'.format("ing_weight",ing_weight,i+1,"answer",answer))
            
#             print('[다리 건너는 중] {4} - {0}:{1} / {2}:{3} / {5}:{6}'.format("ing_truck",ing_truck,"ing_weight",ing_weight,i+1,"answer",answer))
#             answer += 1  

#         #다리를 건넌 트럭은 빼줌
#         end_truck = ing_truck.popleft()
#         ing_weight -= end_truck
#         count += 1
#         #print('\n[다리 다건넘] {0}:{1} / {2}:{3} / {4}:{5}\n-----------------\n'.format("ing_truck",ing_truck,"ing_weight",ing_weight,"answer",answer))
        

#     return answer

# # bridge_length/ weight/ truck_weights
# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


#다리를 건너는 트럭
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing_truck = [0] * bridge_length  #다리 위에 있는 트럭을 나타내는 리스트 : ing_truck
    
    while len(ing_truck)!=0:  #다리에 있는 트럭의 개수가 0이 될때까지 반복
        answer+=1
        ing_truck.pop(0)  #첫번째 요소 pop 해서 한칸씩 이동하기
        # 대기 중인 트럭이 존재하면 : truck_weight
        if (truck_weights):
            if (sum(ing_truck) + truck_weights[0] <= weight): # (다리 위에 있는 트럭 무게 + 대기중인 첫번째 트럭 무게)가 다리의 한계보다 작으면
                ing_truck.append(truck_weights.pop(0)) # 대기중인 트럭 pop 해서 다리위에 올려주기
            else:
                #다리의 한계보다 크면 0을 삽입해서 대기하기
                ing_truck.append(0)

    return answer

# bridge_length/ weight/ truck_weights
print(solution(5, 5, [2, 2, 2, 1, 1, 1, 1, 1]))
# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


