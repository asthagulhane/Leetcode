class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            # Calculate max gain from subtrees; ignore negative sums
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Update the global maximum path sum
            max_path = max(max_path, node.val + left + right)

            # Return the max single-branch path sum to parent
            return node.val + max(left, right)

        dfs(root)
        return max_path
