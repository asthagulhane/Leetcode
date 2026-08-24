import heapq

class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half of numbers (negated to simulate max-heap in Python)
        self.small = []
        # min_heap stores the larger half of numbers
        self.large = []  

    def addNum(self, num: int) -> None:
        # Push to max-heap first, then move the largest element of small half to large half
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Maintain size balance: small heap can have at most 1 more element than large heap
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
