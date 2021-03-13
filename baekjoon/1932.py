#정수 삼각형
#https://www.acmicpc.net/problem/1932
#dp

import sys
input = sys.stdin.readline

n = int(input().rstrip())
length = int((n**2+n)/2) + 1
triangle = [-1]
max_triangle = [0] * length

for _ in range(n):
    row = list(map(int,input().rstrip().rsplit()))
    
    for num in row:
        triangle.append(num)

if n==1:
    print(triangle[1])
    sys.exit(0)

for i in range(n,0,-1):
    start = int((i ** 2 - i + 2) / 2)
    end = int((i**2+i)/2)
    if i==n:
        for j in range(start,end,1):
            # print('왼쪽:',triangle[j],"/오른쪽:",triangle[j+1],"/위에",triangle[j-i+1])
            max_triangle[j-i+1] = max(
                triangle[j]+triangle[j-i+1],
                triangle[j+1]+triangle[j-i+1],
                max_triangle[j-i+1]
            )
    else:
        for j in range(start,end,1):
            # print('왼쪽:',triangle[j],"/오른쪽:",triangle[j+1],"/위에",triangle[j-i+1])
            max_triangle[j-i+1] = max(
                max_triangle[j]+triangle[j-i+1],
                max_triangle[j+1]+triangle[j-i+1],
                max_triangle[j-i+1]
            )

        #print('왼쪽:',triangle[j],"/오른쪽:",triangle[j+1],"/위에",triangle[j-i+1],"/더한값",max_triangle[j-i-1])

print(max_triangle[1])