# 스티커
# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 2행 n열
    n = int(input())
    stickers = []

    for _ in range(2):
        stickers.append(list(map(int, input().rsplit())))

    # dp[0][i] : 0행 i열까지의 최대값, dp[1][i] : 1행 i열까지의 최대값
    dp = [[0 for _ in range(n)] for _ in range(2)]

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
    elif n == 2:
        print(max(stickers[0][0] + stickers[1][1],
              stickers[1][0] + stickers[0][1]))
    else:
        dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
        dp[0][1], dp[1][1] = stickers[0][1] + \
            stickers[1][0], stickers[0][0] + stickers[1][1]

        '''
        dp[0][i]는 현재 위치의 스티커 값(stickers[0][i]) + 
            max( 현재 스티커의 이전 열 대각선 위치, 
                 2열 전의 0행, 
                 2열 전 1행 )
        2열 전도 고려해주는 이유는 이전 열에서 선택하지 않을 수도 있기 때문이다.
        '''
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + stickers[0][i]
            dp[1][i] = max(dp[0][i-1], dp[1][i-2], dp[0][i-2]) + stickers[1][i]

        print(max(dp[0][n-1], dp[1][n-1]))
        # for row in dp:
        #     print(row)
        # print()
