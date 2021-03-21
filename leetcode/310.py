#310. Minimum Height Trees
#https://leetcode.com/problems/minimum-height-trees/
#이진트리

import collections

def findMinHeightTrees(n, edges):
    # 예외 처리
    if n <= 1:
        return [0]
    
    # 양방향 그래프 구성
    graph = collections.defaultdict(list)
    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 첫번째 리프 노드를 leaves 리스트에 추가
    leaves = []
    for i in range(n+1):
        if len(graph[i])==1:
            leaves.append(i)
    
    # 루트 노드만 남을 때까지 반복해서 리프 노드를 제거해준다
    while n > 2:
        n -= len(leaves)
        new_leaves = []

        # 리프노드 leaf
        for leaf in leaves:
            # 리프노드와 연결된 노드 neighbor ( = 다음 리프 노드가 됨 )
            # 그래프에서 leaf를 지워준다.
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            # 만약 neighbor이 리프노드가 되면, new_leaves에 추가해준다.
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        
        # 새로운 리프노드를 할당해준다.
        leaves = new_leaves

    return leaves





print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
# [1]
print(findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))
# [3,4]