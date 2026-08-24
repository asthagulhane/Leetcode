class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left) 
            right = dfs(node.right)    

            rob_curr = node.val + left[1] + right[1]

            skip_curr = max(left) + max(right)
        
            return (rob_curr, skip_curr)

        return max(dfs(root))        