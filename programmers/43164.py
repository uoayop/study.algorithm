#여행경로
#dfs
#https://programmers.co.kr/learn/courses/30/lessons/43164
import collections

def solution(tickets):
    graph = collections.defaultdict(list)

    for start,end in sorted(tickets):
        graph[start].append(end)

    route = []
    def dfs(ticket):
        while graph[ticket]:
            dfs(graph[ticket].pop(0))
        route.append(ticket)

    dfs('ICN')
    return route[::-1]


#<----- 테스트 케이스 ------->

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# #['ICN', 'JFK', 'HND', 'IAD']
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# #['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']
# print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
# #['ICN', 'B', 'ICN', 'A']
# print(solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A", "C"]]))
# #['ICN', 'A', 'ICN', 'A', 'C']
# print(solution([["ICN", "A"], ["A", "B"], ["A", "ICN"], ["ICN", "A"], ["B", "A"]]))
# #['ICN', 'A', 'B', 'A', 'ICN', 'A']
# print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
# #['ICN', 'A', 'D', 'B', 'A', 'C']

print(solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]))
# ['ICN', 'B', 'ICN', 'A', 'D', 'A']
print(solution([['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]))
#['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO']


#<----- 중복 고려가 안 된 코드 ------->
# def dfs(graph,start,answer,saving,goal):
#     if graph[start]==[]:
#         print("if문")
#         if len(answer)==goal:
#             return answer
#         else:
#             print("else문")
#             while saving:
#                 temp = saving.pop()
#                 graph[temp[0]].append(temp[1])
#             dfs(graph,'ICN',answer,[],goal)

#     print(graph)
#     while (graph[start]):
#         ticket = graph[start].pop(0)
#         saving.append([start,ticket])
#         if ticket not in graph:
#             graph[start].append(ticket)
#             ticket = graph[start].pop(0)
        
#         answer.append(ticket)
#         dfs(graph,ticket,answer,saving,goal)

# def solution(tickets):
#     graph = {}
#     answer = ['ICN']
#     saving = []
#     goal = len(tickets)

#     for ticket in sorted(tickets):
#         start, end = ticket[0], ticket[1]
#         if start not in graph:
#             graph[start]=[end]
#         else:
#             graph[start].append(end)
    
#     dfs(graph,'ICN',answer,saving,goal)

#     return answer