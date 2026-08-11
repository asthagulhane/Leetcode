class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            current_sum = 0 

            for  j in range (i + 1):
                current_sum += nums[j]

            result.append(current_sum)

        return result