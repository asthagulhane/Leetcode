# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None -> structurally identical so far
        if not p and not q:
            return True
        
        # One node is None but the other is not -> mismatch in structure
        if not p or not q:
            return False
            
        # Values match, check if left and right subtrees match recursively
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
