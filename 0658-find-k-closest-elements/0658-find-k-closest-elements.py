class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort by distance to x, then by value
        arr.sort(key=lambda num: (abs(num - x), num))
        
        # Slice the first k elements
        result = arr[:k]
        
        # Sort the final result in ascending order
        result.sort()
        return result
