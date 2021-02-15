#K 경유지 내 가장 저렴한 항공권
#최단 경로 문제
#https://leetcode.com/problems/cheapest-flights-within-k-stops/

import collections
import heapq
# 경유지 수 n / 항공권 flights : [출발지,도착지,가격]
# 시작점 src / 도착점 dst / 거칠수있는 경유지 개수 k

def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    for u,v,w in flights:
        graph[u].append((v,w))

    # 큐 변수 : [(가격, 정점, 이동 가능한 남은 경유지 수)]
    Q = [(0,src,K)]

    while Q:
        price, node, k = heapq.heappop(Q)

        # 현재 노드가 도착지면 결과를 리턴함
        if node == dst:
            return price
        
        # k 이내일때만 우선순위 큐에 경로를 추가하도록함
        if k >= 0:
            for v,w in graph[node]:
                alt = price + w
                heapq.heappush(Q,(alt,v,k-1))

    return -1

print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))