#수 정렬하기
#시간 복잡도가 O(nlogn)

#------------병합정렬 사용------------
#분할정복과 재귀 이용
#https://ratsgo.github.io/data%20structure&algorithm/2017/10/03/mergesort/

# import sys

# n=int(sys.stdin.readline().rstrip())
# unsorted_list=[]
# sorted_list=[]

# #리스트 요소가 1개가 될때까지 나눔 / 왼쪽,오른쪽 merge
# def merge_sort(list):
#     if len(list) <= 1:
#         return list
#     mid = len(list) // 2
#     leftList = list[:mid]
#     rightList = list[mid:]
#     leftList = merge_sort(leftList)
#     rightList = merge_sort(rightList)
#     return merge(leftList, rightList)

# #분리한 왼쪽리스트, 오른쪽 리스트의 각각 첫번째 요소를 비교해 작은 값을 결과 리스트에 저장
# #저장한 값은 리스트에서 지움. 
# #left,right에 요소가 하나도 안남을 때까지 반복
# def merge(left, right):
#     result = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 left = left[1:]
#             else:
#                 result.append(right[0])
#                 right = right[1:]
#         elif len(left) > 0:
#             result.append(left[0])
#             left = left[1:]
#         elif len(right) > 0:
#             result.append(right[0])
#             right = right[1:]
#     return result

#     # if (len(arr)<2):
#     #     return arr

#     # mid = len(arr) // 2
#     # low_arr = merge_sort(arr[:mid])
#     # high_arr = merge_sort(arr[mid:])

#     # merged_arr=[]
#     # l=h=0

#     # while l < len(low_arr) and h < len(high_arr):
#     #     if (low_arr[l] < high_arr[h]):
#     #         merged_arr.append(low_arr[l])
#     #         l+=1
#     #     else:
#     #         merged_arr.append(high_arr[h])
#     #         h+=1
#     # merged_arr += low_arr[l:]
#     # merged_arr += high_arr[h:]
#     # return merged_arr


# for i in range(n):
#     num=int(sys.stdin.readline())
#     unsorted_list.append(num)

# sorted_list=merge_sort(unsorted_list)

# for i in sorted_list:
#     print(i)





#------------힙정렬 사용------------
#https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/
#마지막 레벨을 제외한 모든 레벨이 꽉 채워진 완전이진트리를 기본으로 함

#완전이진트리를 1차열배열로도 표현 가능했을 때
#인덱스가 k인 노드의 왼쪽 자식 인덱스는 2k+1, 오른쪽 자식 인덱스는 2k+2

#1. 주어진 원소로 최대 힙 구성
#2. 최대 힙의 루트노드 (배열 첫번째 요소)와 말단노드 (배열 마지막 요소) 교환
#3. 새 루트 노드에 대해 최대 힙 구성
#4. 원소의 개수만큼 2,3 반복

#루트가 왼쪽노드나, 오른쪽 노드보다 작으면 위치 바꿈

import sys

n=int(sys.stdin.readline().rstrip())
unsorted_list=[]
sorted_list=[]

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)
    # BUILD-MAX-HEAP (A) : 위의 1단계
    # 인덱스 : (n을 2로 나눈 몫-1)~0
    # 최초 힙 구성시 배열의 중간부터 시작하면 
    # 이진트리 성질에 의해 모든 요소값을 
    # 서로 한번씩 비교할 수 있게 됨 : O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)


    # Recurrent (B) : 2~4단계
    # 한번 힙이 구성되면 개별 노드는
    # 최악의 경우에도 트리의 높이(logn)
    # 만큼의 자리 이동을 하게 됨
    # 이런 노드들이 n개 있으므로 : O(nlogn)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

for i in range(n):
    num=int(sys.stdin.readline())
    unsorted_list.append(num)

sorted_list=heap_sort(unsorted_list)

for i in sorted_list:
    print(i)