#https://leetcode.com/problems/diameter-of-binary-tree/
#이진 트리의 직경

def dfs(index,depth,root):
    max_depth = depth
    print("-----[index,depth]",index,depth)
    left = index * 2
    right = (index * 2) + 1

    if left < len(root):
        if root[left] is not None:
            # print("[left]",left)
            return_depth = dfs(left,depth+1,root)
            max_depth = max(max_depth,return_depth)
            
    
    if right < len(root):
        if root[right] is not None:
            # print("[right]",right)
            return_depth = dfs(right,depth+1,root)
            max_depth = max(max_depth,return_depth)
    
    return max_depth


def diameterOfBinaryTree(root):
    if root == []:
        return 0
    elif len(root)<=2:
        return 1
    
    left_depth = dfs(2,1,root)
    right_depth = dfs(3,1,root)

    return (left_depth + right_depth)

print(diameterOfBinaryTree([0,1,2,3,None,None,6,7]))
print(diameterOfBinaryTree([0,1,2,3,4,5]))