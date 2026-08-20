class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count the frequency of each number
        counts = Counter(nums)
        
        # Sort the unique elements by their frequency in descending order
        sorted_elements = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        
        # Return the top k elements
        return sorted_elements[0:k]

        