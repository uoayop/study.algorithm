#https://leetcode.com/problems/maximum-depth-of-binary-tree/
#이진 트리의 최대 깊이

from collections import deque

def maxDepth(root):
    depth = 0

    if root:
        queue = deque()
        queue.append((1,1))

        while(queue):
            index,depth = queue.popleft()
            # print("[index]",index)
            
            left = index * 2
            right = (index * 2) + 1
            if left < len(root):
                # print("[left]",left)
                if root[left] is not None:
                    queue.append((left,depth+1))
            if right < len(root):
                # print("[right]",right)
                if root[right] is not None :
                    queue.append((right,depth+1))

    elif len(root)==1:
        return 1
    elif 1 < len(root) < 4:
        return 2
                
    return depth
        

print(maxDepth([0,3,9,20,None,None,15,7])) #3
print(maxDepth([1,None,2])) #2
print(maxDepth([])) #0
print(maxDepth([0]))    #1