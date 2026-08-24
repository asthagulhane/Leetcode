class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def get_height(node):
            if not node:
                return 0 
            return 1 + max(get_height(node.left), get_height(node.right))

        left_h = get_height(root.left) 
        right_h = get_height(root.right)         

        return (
            abs(left_h - right_h) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )    
        