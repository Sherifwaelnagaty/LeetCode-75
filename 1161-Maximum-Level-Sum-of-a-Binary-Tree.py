# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        m_sum,m_i,idx = root.val,1,1
        q = deque()
        q.append(root)
        while q:
            l_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    l_sum+=node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if l_sum > m_sum:
                m_sum = l_sum
                m_i = idx
            idx+=1
        return m_i