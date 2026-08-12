class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # create a temporary array 
        temp = []

        # Step 1 :collect all non - zero elements
        for num in nums:
            if  num != 0 :
                temp.append(num)

        # Step 2 : Fill the remaining place with order
        while len(temp) < len(nums):
            temp.append(0)
        
        # Step 3: Copy the elements back into the original array
        for i in range(len(nums)):
            nums[i] = temp[i]

       
