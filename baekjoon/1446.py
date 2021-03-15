#지름길
#최단거리 
#https://www.acmicpc.net/problem/1446

import sys
import collections
input = sys.stdin.readline


# < 거리를 시작 지점에서 1씩 이동하면서 각 지점에 대한 다익스트라 처리하기 >
# 1씩 이동하면서  if (그 지점에 지름길이 있으면 )
#   : 해당 지점에서 지름길을 타고 도착하는 경우 vs 현재 다익스트라 배열에 저장된 값을 비교 --> 최솟값으로 갱신함
# else (그 지점에 지름길이 없으면)
#   : 이전 지점 + 1 vs 현재 지점 다익스트라 배열에 저장된 값을 비교 --> 최솟값으로 갱신

'''
* 해당 지점에 지름길이 있을 때
지름길을 타고 도착하는 경우 vs ```현재 moved_distance``` 값 중 더 작은 값으로 갱신해준다.
* 해당 지점에 지름길이 없을 때
```moved_distance[다음 지점(;해당 지점 + 1)]``` 값이 ```현재 moved_distance + 1``` 보다 크면 
```moved_distance[다음 지점]``` 의 값을 ```moved_distance[현재 지점] + 1``` 로 갱신해준다.
'''

#지름길 개수 n, 고속도로 길이 d
n, d = map(int,input().rstrip().rsplit())
graph = [[] for _ in range(n)]
# 다익스트라 배열과 비교해서 더 작은 값을 배열에 넣어야하므로 큰 값으로 배열을 초기화 해준다.
moved_distance = [99999 for _ in range(d+1)]

for i in range(n):
    start, end, length = map(int,input().rstrip().rsplit())
    graph[i]=(start,end,length)
graph.sort()
# 그래프의 값들을 정렬해준다. (start,end,length) 순으로

def drive():
    now_length = 0
    now_index = 0
    moved_distance[0] = 0

    while now_length < d:
        while now_index < n:
            start, end, length = (graph[now_index])[0], (graph[now_index])[1], (graph[now_index])[2]

            if start != now_length:
                break
            if end <= d:
                # 지름길로 이동
                compare = moved_distance[now_length] + length
                if compare < moved_distance[end]:
                    moved_distance[end] = compare

            now_index += 1
        
        # 한칸 이동
        if moved_distance[now_length] + 1 < moved_distance[now_length + 1] :
            moved_distance[now_length + 1] = moved_distance[now_length] + 1

        now_length += 1

    print(moved_distance[d])

drive()