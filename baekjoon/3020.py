# 개똥벌레
# https://www.acmicpc.net/problem/3020
# 이분탐색

import sys
input = sys.stdin.readline

def check(height, cave):
    # 개똥벌레 높이가 height일때
    l, r = 0, len(cave) - 1
    while l <= r:
        mid = (l + r) // 2
        if cave[mid] <= height:
            l = mid + 1
        else:
            r = mid - 1

    # height보다 큰 요소의 개수는 부딪히는 장애물의 개수다.
    # 이분탐색이 끝나고 났을 때 r은 height보다 작은 값이 위치한 인덱스를 반환한다.
    # 따라서 (list의 길이 - r + 1)을 빼주면 된다.

    # print("[height]:",height,"[cave]:",cave)
    # print("[l]:{0}, [r]:{1}, [mid]:{2}".format(l,r,mid))
    return len(cave) - (r + 1)


n, h = map(int, input().rsplit())
h_arr, l_arr = [], []

for i in range(n):
    t = int(input())
    if i % 2 == 0:
        l_arr.append(t)
    else:
        h_arr.append(t)

l_arr.sort()
h_arr.sort()

answer, answer_cnt = sys.maxsize, 0

# 어쨌든 모든 높이는 순차탐색을 해야함
for i in range(1, h+1):
    l_cnt = check(i-1, l_arr)
    h_cnt = check(h-i, h_arr)
    cur_cnt = l_cnt + h_cnt

    if cur_cnt < answer:
        answer = cur_cnt
        answer_cnt = 1
    elif cur_cnt == answer:
        answer_cnt += 1
    else:
        pass

print(answer, answer_cnt)

'''
20 10
5
5
6
4
6
7
9
1
4
4
9
4
9
3
7
1
5
1
6
5


10 9
'''

'''
6 5
1
3
4
2
2
3




'''
