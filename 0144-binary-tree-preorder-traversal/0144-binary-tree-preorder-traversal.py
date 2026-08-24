# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:                                                                
#             return []
#         return ( 
#             [root.val]
#             + self.preorderTraversal(root.left)
#             + self.preorderTraversal(root.right)
#         ) 



class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res        













    
        
        