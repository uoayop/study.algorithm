#네트워크
#https://programmers.co.kr/learn/courses/30/lessons/43162

import sys

def solution(n, computers):
    graph = {}
    visited= [0]* n
    answer = 0

    for row_index,rows in enumerate(computers):
        for num_index,num in enumerate(rows):
            if num==1 :
                if row_index not in graph:
                    graph[row_index]=[num_index]
                else:
                    graph[row_index].append(num_index)

    #print(graph)

    def dfs(index):
        #방문한 곳이 아니므로 연결되어 있지 않다 = 다른 네트워크이므로 return 1
        if visited[index]==0:
            visited[index] = 1
            while (graph[index]):
                dfs(graph[index].pop(0))
            return 1
        #방문한 곳이므로 연결되어 있다 = 같은 네트워크이므로 return 0
        else: 
            return 0
            


    for i in range(n):
        answer += dfs(i)
        
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4,[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
