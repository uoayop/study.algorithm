# 숫자카드
# https://www.acmicpc.net/problem/10815
# 이진 탐색

import sys
input = sys.stdin.readline

# 상근이가 갖고 있는 숫자 카드 n개
# 체크 해야하는 숫자 카드 m개

n = int(input())
cards = list(map(int, input().rsplit()))

m = int(input())
check = list(map(int, input().rsplit()))

cards.sort()
l, r = 0, n-1

for c in check:
    l, r = 0, n-1
    flag = False
    while l <= r:
        mid = (l + r) // 2
        if cards[mid] < c:
            l = mid + 1
        elif cards[mid] > c:
            r = mid - 1
        else:
            flag = True
            break
    if flag:
        print(1,end=' ')
    else:
        print(0,end=' ')
print()

# class Tree:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def toBST(lst):
#     if not lst:
#         return None

#     mid = len(lst) // 2

#     node = Tree(lst[mid])
#     node.left = toBST(lst[:mid])
#     node.right = toBST(lst[mid + 1:])

#     return node


# BST = toBST(sorted(cards))

# # DFS 전위 순회
# # def preorder(node):
# # 	if node is None:
# # 		return
# # 	preorder(node.left)
# # 	print(node.val)
# # 	preorder(node.right)

# # preorder(BST)

# for c in check:
#     # print(">> c:",c)
#     curr = BST
#     curr_val = curr.val
#     flag = False

#     while curr is not None:
#         curr_val = curr.val
#         # print(">",curr_val)
#         if curr_val < c:
#             curr = curr.right
#         elif curr_val > c:
#             curr = curr.left
#         else:
#             flag = True
#             break
#     if flag:
#         print(1,end=' ')
#     else:
#         print(0,end=' ')
# print()
