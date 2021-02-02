#15953 상금헌터

import sys

def f1_money(a):
    if (a==1):
        return f1[0]
    elif (a==2 or a==3):
         return f1[1]
    elif (4<=a and a<=6) :
         return f1[2]
    elif (7<=a and a<=10) :
         return f1[3]    
    elif (11<=a and a<=15) :
         return f1[4]   
    elif (16<=a and a<=21):
         return f1[5]
    else:
        return 0 

def f2_money(a):
    if (a==1):
        return f2[0]
    elif (a==2 or a==3):
         return f2[1]
    elif (4<=a and a<=7) :
         return f2[2]
    elif (8<=a and a<=15) :
         return f2[3]    
    elif (16<=a and a<=31) :
         return f2[4]   
    else:
        return 0 


f1= [5000000,3000000,2000000,500000,300000,100000]
f2= [5120000,2560000,1280000,640000,320000]

T = int(sys.stdin.readline().rstrip())

for i in range(0,T):
    money = 0
    order = sys.stdin.readline().rstrip().split()
    a = int(order[0])
    b= int(order[1])

    money = f1_money(a)+f2_money(b)

    print(money)
