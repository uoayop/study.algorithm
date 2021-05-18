# 공유기 설치
# https://www.acmicpc.net/problem/2110
# 이진탐색

# https://claude-u.tistory.com/448 어렵다잉
import sys
input = sys.stdin.readline

# c개의 공유기를 n개의 집에 설치, 가장 인접한 두 공유기 사이의 최대 거리 구하기
n, c = map(int,input().rsplit())
position = []
result = 0

for _ in range(n):
    position.append(int(input()))
position.sort()

def counter(distance):
    cnt = 1
    curr_p = position[0]
    for i in range(1, n):
        # (현재 위치 + 거리) 가 다음 위치 거리보다 짧으면 공유기 개수 + 1
        if curr_p + distance <= position[i]:
            cnt += 1
            curr_p = position[i]
    return cnt

# r : 가장 먼 집 사이의 거리
l, r = 0, position[-1] - position[0]

while l <= r:
    mid = (l + r) // 2
    print(">>c:{3}, mid:{0}, l:{1}, r:{2}".format(mid,l,r,c))

    # 공유기 개수가 c와 같거나 많으므로 거리를 늘려준다.
    if counter(mid) >= c:
        result = max(result, mid)
        l = mid + 1
    # 공유기 개수가 c보다 적으므로 거리를 좁혀준다.
    else:
        r = mid - 1

print(result)