import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        # Add the original index to each task and sort by enqueue time
        ext_tasks = sorted([t + [i] for i, t in enumerate(tasks)])
        
        res, min_heap = [], []
        time = i = 0
        n = len(tasks)
        
        while len(res) < n:
            # If no tasks are available yet, fast-forward time to the next task's arrival
            if not min_heap and time < ext_tasks[i][0]:
                time = ext_tasks[i][0]
                
            # Push all tasks that have arrived by the current time into the min-heap
            while i < n and ext_tasks[i][0] <= time:
                heapq.heappush(min_heap, (ext_tasks[i][1], ext_tasks[i][2]))
                i += 1
                
            # Process the task with the shortest processing time
            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            res.append(idx)
                
        return res
