# 1406 에디터

# 시간초과
# import sys

# def deleteText(string,n):
#     begin=string[:n]
#     end=string[n+1:]
#     return begin+end

# def insertTest(string,n,str):
#     begin=string[:n]
#     end=string[n:]
#     return begin+str+end


# text= sys.stdin.readline().rstrip()
# length= len(text)
# T = int(sys.stdin.readline())
# cs=length

# for i in range(0,T):
#     orders = sys.stdin.readline().rstrip().split()
#     order=orders[0]
#     if (order=='L'):
#         if (cs!=0):
#             cs-=1
#     elif (order=='D'):
#         if (cs!=length-1):
#             cs+=1
#     elif (order=='B'):
#         if (cs!=0):
#             text=deleteText(text,cs-1)
#             cs-=1
#     elif (order=='P'):
#         t=orders[1]
#         text=insertTest(text,cs,t)
#         cs+=1

# print(text)
    
import sys  

leftText= list(''.join(sys.stdin.readline().rstrip()))
rightText=[]

T = int(sys.stdin.readline())

for i in range(T):
    orders = sys.stdin.readline().rstrip().split()
    order=orders[0]
    if (order=='L'):
        if (len(leftText)!=0):
            rightText.append(leftText.pop())
    elif (order=='D'):
        if (len(rightText)!=0):
            leftText.append(rightText.pop())
    elif (order=='B'):
        if (len(leftText)!=0):
            leftText.pop()
    elif (order=='P'):
        leftText.append(orders[1])

rightText.reverse()
result = leftText + rightText
result_str=""

for _ in range (len(result)):
    result_str += result[_]

print(result_str)