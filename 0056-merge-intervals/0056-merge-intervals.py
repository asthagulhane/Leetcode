class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals :
            return[]

        intervals.sort(key= lambda x: x[0])

        merge = []

        # initialize
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]

        for i  in range(1,len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]

            if next_start <= curr_end  :
                curr_end = max(curr_end,next_end)

            else:
                # overlap the array 
                merge.append([curr_start,curr_end])
                curr_start = next_start
                curr_end = next_end
        merge.append([curr_start,curr_end]) 
        return merge
            

