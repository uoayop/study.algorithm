import sys

#이진탐색
n = int(sys.stdin.readline().rstrip())
nums = sorted(map(int, input().split()))
x = int(sys.stdin.readline().rstrip())

ansCount = 0

left = 0
right = n-1

while left != right:
    sum = nums[left]+nums[right]
    if sum==x:
        ansCount+=1
        left+=1
    elif sum > x :
        right-=1
    else:
        left+=1

print(ansCount)
