# #나이순 정렬

# import sys
# import operator

# n=int(sys.stdin.readline().rstrip())
# members={}

# for i in range(n):
#     temp=sys.stdin.readline().rstrip().rsplit()
#     members[temp[1]]=int(temp[0]),temp[1]


# # result=(sorted(list(members.values())))
# result=list(sorted(members.items(),key=operator.itemgetter(0)))

# print(''.join('{0} {1}\n'.format(y,x) for x,y in result))

#내가 구현 안했음..ㅠ
# N = int(input())
# array = []
# for i in range(N):
#     num, name = map(str, input().split())
#     array.append([int(num), name])
# array=sorted(array, key = lambda x:x[0])
# for i in array:
#     print(i[0], i[1])

import sys
input = sys.stdin.readline

n = int(input())

people = []
for i in range(n):
    age, name = map(str,input().rsplit())
    people.append([i,int(age),name])

people.sort(key = lambda x:(x[1],x[0]))

for p in people:
    print(p[1],p[2])