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

    print(graph)

    def dfs(index):
        if visited[index]==0:
            visited[index]=1
            while (graph[index]):
                dfs(graph[index].pop(0))
            return 1
        else: return 0
            


    for i in range(n):
        answer += dfs(i)
        
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4,[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
