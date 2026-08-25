class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(left, right, s=""):
            if left == right == 0:
                return [s]
            
            res = []
            if left > 0:
                res += dfs(left - 1, right, s + "(")
            if right > left:
                res += dfs(left, right - 1, s + ")")
            return res
            
        return dfs(n, n)
