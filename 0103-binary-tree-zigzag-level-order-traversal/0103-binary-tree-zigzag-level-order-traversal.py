# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = deque()
        def dfs(root, level):
            if not root:
                return

            #level already has nodes and is even
            if level <= len(output)-1 and level % 2 == 0:
                output[level].append(root.val)
            
            #level already has nodes and is odd
            elif level <= len(output)-1 and level % 2 != 0:
                output[level].appendleft(root.val)
            
            else:
                output.append(deque([root.val])) #must append as a deque too
            
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        
        dfs(root, 0)
        return output   