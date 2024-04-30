class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            count = 0
            if current_sum == targetSum:
                count += 1
            
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            return count
        
        if not root:
            return 0
        
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
