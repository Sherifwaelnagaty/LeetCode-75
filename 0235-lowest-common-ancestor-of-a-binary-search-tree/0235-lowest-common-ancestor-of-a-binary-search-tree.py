# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True: # Here you don't need to check for node==None because the loop will execute forever but as the 2 given nodes are present in the tree we will some how definitely hit the 1st or 2nd if statement.
            if node.val==p.val or node.val==q.val: #This is for one of the given nodes==present node
                return node
            if (node.val>p.val and q.val>node.val) or (node.val>q.val and node.val<p.val):   #This is for 2 opposite directions
                return node
            if node.val>p.val and node.val>q.val: #Both the values will be present on the left side of the present node
                node=node.left
            if p.val>node.val and q.val>node.val: #Both the values will be present on the right side of the present node
                node=node.right