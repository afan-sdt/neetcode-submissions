class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # approach: remove the interval with the longer end time
        # sort by start, when an overlap is seen, we increment by 1 and choose the interval with a lesser end time
        intervals.sort()
        res = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] > intervals[i][0]:
                res +=1
                if curr[1] > intervals[i][1]:
                    curr = intervals[i]
            else:
                curr = intervals[i]
        return res