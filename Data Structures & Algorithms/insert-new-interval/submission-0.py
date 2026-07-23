class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #check if new interval should be inserted here:
            # end of new is less than interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #new is past the curr
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            #if overlapping, combine
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res


        