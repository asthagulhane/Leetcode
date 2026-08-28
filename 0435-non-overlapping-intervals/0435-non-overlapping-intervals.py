class Solution:

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end times to maximize the number of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # Perfectly aligned indentation block
            if start < prev_end:
                removals += 1
            else:
                prev_end = end

        return removals
