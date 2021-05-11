#k번째 수
#힙
#https://www.acmicpc.net/problem/1300

# ----------메모리 초과
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# k = int(input())
# b = []
# max_len = k // 2

# for i in range(1,max_len+1):
#     for j in range(1,max_len+1):
#         num = i * j
#         heapq.heappush(b, [num,(i,j)])

# for _ in range(k-1):
#     heapq.heappop(b)

# print(heapq.heappop(b)[0])

#https://claude-u.tistory.com/449
# 이분탐색으로 어떤 수보다 작은 수의 곱(i*j)이 몇개인지 알아내면 됨
# a보다 작은 숫자가 몇개인지 찾아내면 a가 몇번째 숫자인지 알아낼 수 있음
# ex) 10*10에서 20보다 작거나 같은 수는
# 1*1 ~ 1*10, 2*1 ~ 2*10, 3*1 ~ 3*6
# 즉 (20 // 1) + (20 // 2) +  (20 // 3) + ...  + (20 // 10) ; 최대 n까지

# 배열을 절반으로 쪼개면서 비교해준다.
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 0, k
# k번째 수는 k를 넘을 수 없다.

while start <= end:
    # print("[start]:{}, [end]:{}".format(start,end))
    mid = (start+end) // 2
    # print("[mid]:",mid)
    cnt = 0

    for i in range(1,n+1):
        # print("[mid//i]:{}, [n]:{}".format(mid//i,n))
        cnt += min(mid//i, n)   
        # mid // i가 n보다 클 수 있기 때문에 최대 n값을 갖게 해줌
    # print("[cnt]:",cnt)   
    if cnt >= k:
        #최솟값을 찾아야하므로 같을 때는 끝범위를 줄여준다.
        answer = mid
        # print("[answer]:",answer)
        end = mid - 1
    else:
        start = mid + 1

print(answer)

