# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        # # starting from 0 index 
        # i = 0 
        # # loop is going till second last element of arr
        # while i < len(nums) -1   :

        #     if nums[i] == nums[i + 1 ] :
        #     # removing the duplicate num from array 
        #         nums.pop(i + 1)

        #     else :
        #         i += 1

               
        # return len(nums)






class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums)) == 0 :
            return 0 

        i = 0 

        for j in range (1,len(nums)):
            if nums[i] != nums[j] :
                i += 1

            nums[i] = nums[j] 
        
        return i + 1










        

















            