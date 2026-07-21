class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # starting from 0 index 
        i = 0 
        # loop is going till second last element of arr
        while i < len(nums) -1   :

            if nums[i] == nums[i + 1 ] :
            # removing the duplicate num from array 
                nums.pop(i + 1)

            else :
                i += 1

               
        return len(nums)
            