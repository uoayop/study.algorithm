# 게임
# https://www.acmicpc.net/problem/1072

import sys
input = sys.stdin.readline

# 게임 횟수 x, 이긴 게임 y, 승률 z
# 최소 몇번 더 해야 승률이 변하는지 구해라 (소수점 버림)
# 절대 안변하면 -1 출력
# 나눗셈 조심!!! https://www.acmicpc.net/board/view/68226

x, y = map(int, input().rsplit())
victory = y * 100 // x
ans = sys.maxsize
l, r = 1, x
print("[victory]:", victory)

while l <= r:
    mid = (l + r) // 2

    curr_vic = (y + mid) * 100 // (x + mid)
    print("[mid]:{0}, [curr_vic]:{1}, [l]:{2}, [r]:{3}".format(
        mid, curr_vic, l, r))

    if curr_vic > victory:
        ans = min(mid,ans)
        r = mid - 1
    else:
        l = mid + 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
