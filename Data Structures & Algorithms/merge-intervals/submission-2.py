class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # CARIT: clarify, approach, runtime, implement, test
        # are the intervals sorted already? we want to sort them by start time
        # are they unique?
        # do we need to do it in place?
        #approach: sort then go through and see if curr overlaps with the next interval
        # if overlap, combine
        # if no overlap, we insert curr and make the next interval current
        # at the end we insert curr
        #test cases: overlaps, not overlaps
        # [1, 3], [3, 5], [9, 10], [6, 7]
        # sort: [1, 3], [3, 5], [6, 7], [9, 10]
        # curr = 
        # next = done
        # res = [1,5] [6, 7] [9 10]

        # runtime: O(nlogn) for the sort and O(n) for the output array

        intervals.sort()

        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] >= intervals[i][0]:
                curr[0] = min(curr[0], intervals[i][0])
                curr[1] = max(curr[1], intervals[i][1])
            else:
                res.append(curr.copy())
                curr[0] = intervals[i][0]
                curr[1] = intervals[i][1]
        res.append(curr.copy())
        return res



