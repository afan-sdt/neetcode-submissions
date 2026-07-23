class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        #sort intervals, by default will be by start
        intervals.sort()
        currInterval = intervals[0]
        res=[]
        for i in range(1, len(intervals)):
            #see if current interval overlaps with iterator
            if currInterval[1] >= intervals[i][0]:
                #combine intervals
                currInterval[0] = min(currInterval[0], intervals[i][0])
                currInterval[1] = max(currInterval[1], intervals[i][1])
            else:
                res.append(currInterval)
                currInterval = intervals[i]
        res.append(currInterval)
        return res
