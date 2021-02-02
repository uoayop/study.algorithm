import sys

inputs = sys.stdin.readline().rsplit()
H, M=int(inputs[0]),int(inputs[1])

if (M-45<0):
    H-=1
    M=M+15
    if (H<0):
        H=23
else:
    M=M-45

print(H,M)
    