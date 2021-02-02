def rotate(arr):
    newArr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newArr[j][N-1-i] = arr[i][j]
    return newArr

T = int(input())
for time in range(1, T+1):

    N = int(input())    # n x n 행렬

    #한 줄씩 arr 배열에 append 해주기 : 첫번째 행은 arr[0],두번째 행은 arr[1]..
    arr = [list(map(int, input().split())) for _ in range(N)]
   
    a = rotate(arr) #90도 회전
    b = rotate(a)   #a 90도 회전 = 180도 회전
    c = rotate(b)   #b 90도 회전 = 270도 회전

    print('#{}'.format(time))
    for i in range(N):
        #원하는 형태로 출력하기 위해서 한줄씩 str으로 바꾼뒤 출력
        print(''.join(map(str,a[i])), ''.join(map(str,b[i])), ''.join(map(str,c[i])))
