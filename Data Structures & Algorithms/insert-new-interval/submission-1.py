class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # CARIT
        # Clarify : what happens when the new interval inserted causes overlaps? we merge
        # What's considered an overlap? are [1,2] and [2,3] considered overlapping or separate?
        # does the intervals array have to be modified in place?
        # Approach: i'm going to iterate through the intervals array and see if the new interval should be inserted here. there are some possibilities: 1) the new interval doesn't overlap with any interval 2) the new interval overlaps with existing intervals in which case we should merge. we compare currInterval to newInterval. 
        #if currInterval ends before start of newInterval, we add it to result and advance.
        # if newInterval and currInterval overlap, we make newInterval the merged of curr and newInterval (i.e min(newStart, currStart), max(newEnd, currEnd)) and we advance. now we are trying to insert this new larger merged individual. 
        #if newInterval ends before the start of curr, we add new interval to the result then currInterval and keep it pushing until the end. honestly we could just return here to cause no problems

        # [1, 3], [4, 6], [9,10] new: [7, 8] -> no overlap
        # [1, 3], [4, 6]  new: [2, 5] -> overlap, needs nerge
        # [1, 3], [4, 6], [9,10] new: [12, 14] -> past end
        # [2, 3], [4, 6], [9,10] new: [0, 1] -> before start
        res = []
        newStart = newInterval[0]
        newEnd = newInterval[1]
        inserted = False
        for currStart, currEnd in intervals:
            if currEnd < newStart or inserted: #no overlap, curr is before keep it pushing
                res.append([currStart, currEnd])
            elif currStart <= newEnd: #overlap, merge curr into new
                newStart = min(currStart, newStart)
                newEnd = max(currEnd, newEnd)
            elif currStart > newEnd: # can insert the new interval now
                res.append([newStart, newEnd])
                res.append([currStart, currEnd])
                inserted = True
        if not inserted:
            res.append([newStart, newEnd])
        return res
        # Runtime: O(n) time and O(n) space for result
        # implement

        # test