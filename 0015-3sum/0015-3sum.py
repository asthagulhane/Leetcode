class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Sorting is mandatory for the two-pointer technique
    
        for i in range(len(nums) - 2):
        # Optimization: If the starting number is > 0, 
        # any numbers after it will also be positive and cannot sum to 0.
            if nums[i] > 0:
                break
            
        # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
        # Set up two pointers for the rest of the array
            left = i + 1
            right = len(nums) - 1
        
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
            
                if current_sum < 0:
                    left += 1  # Sum is too small, move left pointer to increase it
                elif current_sum > 0:
                    right -= 1  # Sum is too large, move right pointer to decrease it
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                            left += 1
                # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                # Move both pointers inward to look for next potential match
                    left += 1
                    right -= 1
                
        return res

        