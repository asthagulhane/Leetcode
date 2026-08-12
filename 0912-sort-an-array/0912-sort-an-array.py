class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(left,right):
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2
            left_half = merge_sort  (left , mid)       
            right_half = merge_sort (mid + 1,right)

            return merge(left_half, right_half)

        def merge(left, right):
            merge = []
            i = j = 0

            while i < len(left) and j < len(right):
                if  left[i] <= right[j]:
                    merge.append(left[i])
                    i += 1
                else:
                    merge.append(right[j])
                    j += 1 
            merge.extend(left[i:])
            merge.extend(right[j:])

            return merge
        return merge_sort(0,len(nums)-1)