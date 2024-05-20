class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def helper(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            helper(node.right, level + 1)
            helper(node.left, level + 1)
        
        helper(root, 0)
        return result
