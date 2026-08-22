class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = [] # Stores pairs of (temp, index)
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append((t, i))
            
        return ans
