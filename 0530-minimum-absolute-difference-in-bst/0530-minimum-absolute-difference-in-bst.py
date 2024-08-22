# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def inorder(troot):
            nonlocal arr
            if not troot:
                return
            inorder(troot.left)
            arr.append(troot.val)
            inorder(troot.right)
        inorder(root)
        x=float("inf")
        for i in range(1,len(arr)):
            x=min(arr[i]-arr[i-1],x)
        return x
        