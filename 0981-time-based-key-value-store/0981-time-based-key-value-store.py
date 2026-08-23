import bisect
from collections import defaultdict

 
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Timestamps are strictly increasing, so they are pre-sorted
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        # Binary search for the rightmost index where timestamp matches or is smaller
        idx = bisect.bisect_right(arr, timestamp, key=lambda x: x[0])
        return arr[idx - 1][1] if idx > 0 else ""
