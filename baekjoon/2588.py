import sys

str_num1=sys.stdin.readline()
str_num2=sys.stdin.readline()

int_num2=[]

for i in range(0,3):
    if i==0:
        int_num2.append(int(str_num2[i]))
    elif i==1:
        int_num2.append(int(str_num2[i]))
    else:
        int_num2.append(int(str_num2[i]))
    
sum_index0=int(str_num1)*int_num2[0]
sum_index1=int(str_num1)*int_num2[1]
sum_index2=int(str_num1)*int_num2[2]

print(sum_index2)
print(sum_index1)
print(sum_index0)
print(sum_index0*100+sum_index1*10+sum_index2)