#단지번호붙이기
#dfs
#https://www.acmicpc.net/problem/2667

N = int(input())
li = [list(input().rstrip()) for _ in range(N)]

ans = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(N):
        if li[i][j] == "1":
            cnt = 1
            li[i][j] = "0"
            q = [(i,j)]
            while q:
                x,y = q.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if li[nx][ny] == "1":
                            q.append((nx,ny))
                            li[nx][ny] = "0"
                            cnt += 1
            ans.append(cnt)
ans.sort()       
print(len(ans))
for i in ans:
    print(i)
