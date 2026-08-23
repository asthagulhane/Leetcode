class Solution:

    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)

        #Handles both odd and even lengths seamlessly
        return (merged[n // 2] + merged [(n-1) // 2]) / 2
        