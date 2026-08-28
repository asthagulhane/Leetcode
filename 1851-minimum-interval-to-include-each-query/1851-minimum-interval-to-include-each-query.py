import heapq


class Solution:

    def minInterval(
        self, intervals: list[list[int]], queries: list[int]
    ) -> list[int]:
        # 1. Sort intervals by their start times
        intervals.sort()

        # 2. Pair each query with its original index
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        min_heap = []  # Elements inside: (size_of_interval, end_time)
        i = 0  # Pointer for intervals

        # 3. Process queries in ascending order
        for q, query_idx in sorted_queries:

            # FIX 1: Compare against interval start time intervals[i][0]
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                i += 1

            # FIX 2: Check the end time of the smallest interval at heap top [0][1]
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # FIX 3: Retrieve the size of the smallest interval at heap top [0][0]
            if min_heap:
                res[query_idx] = min_heap[0][0]

        return res
