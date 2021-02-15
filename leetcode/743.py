#네트워크 딜레이 타임
#최단 경로 문제
#https://leetcode.com/problems/network-delay-time/

import sys
import collections
import heapq

def networkDelayTime(times, n, k):
    # 그래프 인접 리스트 구성
    graph = collections.defaultdict(list)
    for u,v,w in times:
        graph[u].append((v,w))

    # 큐 변수 : [(소요시간, 정점)]
    Q = [(0,k)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time,node = heapq.heappop(Q)
        if node not in dist:
            dist[node]=time
            for v,w in graph[node]:
                alt = time + w
                heapq.heappush(Q,(alt,v))
    
    if len(dist)== n :
        return max(dist.values())
        #dist를 출력하면 {2: 0, 1: 1, 3: 1, 4: 2} 이렇게 나옴 [node : time]
    return -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))