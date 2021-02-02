#수 정렬하기
#시간 복잡도가 O(n²)

#------------sorted 함수 사용------------
# import sys

# n=int(sys.stdin.readline().rstrip())
# result=[]

# for i in range(n):
#     num=int(sys.stdin.readline())
#     result.append(num)

# result=(sorted(result))
# for i in result:
#     print(i)

#------------삽입정렬------------
#https://www.daleseo.com/sort-insertion/
# import sys

# n=int(sys.stdin.readline().rstrip())
# unsorted_list=[]
# sorted_list=[]

# def insertion_sort(arr):
#     for end in range(1,len(arr)):
#         for i in range(end,0,-1):
#             if (arr[i-1] > arr[i]):
#                 arr[i-1],arr[i] = arr[i],arr[i-1]
#     return arr

# for i in range(n):
#     num=int(sys.stdin.readline())
#     unsorted_list.append(num)

# sorted_list=insertion_sort(unsorted_list)

# for i in sorted_list:
#     print(i)

#------------거품정렬------------
#https://www.daleseo.com/sort-bubble/
import sys

n=int(sys.stdin.readline().rstrip())
unsorted_list=[]
sorted_list=[]

def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        # 전체루프는 4번
        for j in range(0,len(arr)-i-1):
            # 안쪽루프는 전체루프가 돌때마다 4번->3번->2번->1번으로 줄어듬
            # 따라서 len-i-1
            if (arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

for i in range(n):
    num=int(sys.stdin.readline())
    unsorted_list.append(num)

sorted_list=bubble_sort(unsorted_list)

for i in sorted_list:
    print(i)