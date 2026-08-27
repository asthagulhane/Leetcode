class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = current = 0
        
        for i in range(len(arr)):
            # If the last three elements form a valid peak or valley
            if i >= 2 and (arr[i-2] > arr[i-1] < arr[i] or arr[i-2] < arr[i-1] > arr[i]):
                current += 1
            # If it's a new alternating pair (not equal)
            elif i >= 1 and arr[i-1] != arr[i]:
                current = 2
            # Base case or flatline reset
            else:
                current = 1
                
            ans = max(ans, current)
            
        return ans

        