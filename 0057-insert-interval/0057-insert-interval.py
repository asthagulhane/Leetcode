class Solution:

    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        res = []
        new_start, new_end = newInterval

        for i, (start, end) in enumerate(intervals):
            # 1. Current interval ends before newInterval starts
            if end < new_start:
                res.append([start, end])
            # 2. Current interval starts after newInterval ends
            elif start > new_end:
                return res + [[new_start, new_end]] + intervals[i:]
            # 3. Overlapping intervals, merge them into newInterval
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        res.append([new_start, new_end])
        return res
