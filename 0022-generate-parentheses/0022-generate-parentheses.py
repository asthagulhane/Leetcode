# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         def dfs(left, right, s=""):
#             if left == right == 0:
#                 return [s]
            
#             res = []
#             if left > 0:
#                 res += dfs(left - 1, right, s + "(")
#             if right > left:
#                 res += dfs(left, right - 1, s + ")")
#             return res
            
#         return dfs(n, n)




class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, current_str):
            # Base case: valid combination found
            if open_count == close_count == n:
                res.append(current_str)
                return
            
            # Add an open parenthesis if we haven't reached the limit
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Add a close parenthesis if it won't violate well-formed rules
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")
                
        backtrack(0, 0, "")
        return res
