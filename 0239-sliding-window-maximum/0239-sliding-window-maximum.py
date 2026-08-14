class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
            
        result = []
        q = deque()  # Stores indices of elements
        
        for i in range(len(nums)):
            # 1. Remove ihndices that are out of the current window's left boundary
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Remove smaller elements from the back because they can't be the max
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            # 3. Add the current elementss index to the back of the queue
            q.append(i)
            
            # 4. Once the first window is fully formed, start adding the max to result
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result


        