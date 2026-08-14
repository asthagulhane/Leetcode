# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         nums1[m:] = nums2 

#         nums1.sort()






class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1       # Last valiid element in nums1
        p2 = n - 1       # Last element in nums2
        p = m + n - 1    # Last position in nums1
        
        # Move backwards through both arrays
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
       
        