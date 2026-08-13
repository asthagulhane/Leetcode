# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         # Handle cases where k is greater than the array length
#         k = k % n  
        
#         # Rotate the array by 1 step, k times
#         for _ in range(k):
#             # Store the last element
#             last_element = nums[n - 1]
            
#             # Shift all elements to the right by 1
#             for i in range(n - 1, 0, -1):
#                 nums[i] = nums[i - 1]
                
#             # Place the last element at the front
#             nums[0] = last_element










class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len (nums)
        k %= n 
        def reverse(left:int , right:int) -> None:
            while left < right:
                nums[left] ,nums[right] = nums[right] , nums[left]
                left += 1 
                right -= 1
        # step 1 :reversiomg the array 
        reverse(0, n - 1)

        # step 2 : reverssing the first k elements
        reverse(0, k - 1)

        # step 3 :reverse the remaining elements
        reverse(k, n - 1)













