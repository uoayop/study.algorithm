#https://leetcode.com/problems/valid-palindrome/
import collections
import re

# def isPalindrome(s: str) -> bool:
#     result = []
#     for char in s:
#         if char.isalnum():
#             result.append(char.lower())
#
#     while len(result) > 1:
#         if (result.pop(0) != result.pop()):
#             return False
#     return True
#
#
# s= "A man, a plan, a canal: Panama"
# print(isPalindrome(s))



# def isPalindrome(s: str) -> bool:
#     deq=collections.deque()
#     for char in s:
#         if char.isalnum():
#             deq.append(char.lower())
#
#     while len(deq) > 1:
#         if (deq.popleft() != deq.pop()):
#             return False
#     return True
#
#
# s= "A man, a plan, a canal: Panama"
# print(isPalindrome(s))


def isPalindrome(s: str) -> bool:
    s=s.lower()
    s=re.sub('[^a-z0-9]','',s)  #불필요한 문제 필터링
    return s==s[::-1]


s= "A man, a plan, a canal: Panama"
print(isPalindrome(s))