def fibo(n):
    result = [0] * (n+1)
    for i in range(1,n+1):
        if i==1 or i==2:
            result[i]=1
        else:
            result[i] = result[i-1] + result[i-2]
    return result[n]

def solution(n):
    print(fibo(3))