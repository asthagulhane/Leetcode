from collections import Counter
from typing import List


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        counts = Counter(tasks).values()

        # Find the maximum frequency
        max_freq = max(counts)

        # Count how many tasks have that maximum frequency
        max_freq_tasks = list(counts).count(max_freq)

        # Calculate the minimum intervals required based on the formula
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)
