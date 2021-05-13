#트리의 지름
#dfs, ..
#https://www.acmicpc.net/problem/1167


# # --------- 시간초과
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# cnt = int(input())
# graph = defaultdict(list)

# for _ in range(cnt):
#     temp = list(map(int,input().rsplit()))
#     key = temp[0]
#     for i in range(1,len(temp)-1,2):
#         graph[key].append((temp[i],temp[i+1]))

# max_cnt = 0
# def dfs(node,cnt):
#     global max_cnt
#     max_cnt = max(max_cnt, cnt)
#     visited[node] = True
#     for u,c in graph[node]:
#         if not visited[u]:
#             dfs(u,cnt+c)

# answer = 0
# for node in range(1,cnt+1):
#     visited = [False] * (cnt+1)
#     dfs(node,0)

# print(max_cnt)

"""
"트리의 지름을 구하는 공식은 임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고, 이 노드 B에서 가장 거리가 먼 노드 C를 구하게 되었을 때, B와 C 사이의 거리가 트리의 지름이 된다."
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

cnt = int(input())
graph = defaultdict(list)

for _ in range(cnt):
    temp = list(map(int,input().rsplit()))
    key = temp[0]
    for i in range(1,len(temp)-1,2):
        graph[key].append((temp[i],temp[i+1]))

max_cnt = 0
far_node = 0
def dfs(node,cnt):
    global max_cnt
    global far_node
    if max_cnt < cnt :
        max_cnt = cnt
        far_node = node

    visited[node] = True
    for u,c in graph[node]:
        if not visited[u]:
            dfs(u,cnt+c)

visited = [False] * (cnt+1)
dfs(1,0)
visited = [False] * (cnt+1)
dfs(far_node,0)

print(max_cnt)