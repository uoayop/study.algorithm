import sys

# T=int(sys.stdin.readline())
#
# for i in range(T):
#     test_case=sys.stdin.readline().rstrip()
#     if (test_case==test_case[::-1]):
#         print('#%d'%(i+1),1)
#     else:
#         print('#%d'%(i+1),0)


T=int(sys.stdin.readline())

for i in range(T):
    test_case=input()
    if (test_case==test_case[::-1]):
        print('#%d'%(i+1),1)
    else:
        print('#%d'%(i+1),0)