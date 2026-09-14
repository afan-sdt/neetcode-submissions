"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #basically we need to determine what is the maximum number of overlaps
        # we can split up the intervals into start times and end times
        # we increment our counter when a meeting is started
        # we decrement our counter when a meeting is ended
        # our result is the maximum value of our counter
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        heapq.heapify(starts)
        heapq.heapify(ends)
        counter = 0
        res = 0
        while starts or ends:
            
            if starts and ends and starts[0] < ends[0]:
                counter += 1
                heapq.heappop(starts)
                res = max(res, counter)
            elif starts and ends and ends[0] < starts[0]:
                counter -= 1
                heapq.heappop(ends)
            elif starts and ends and ends[0] == starts[0]:
                heapq.heappop(starts)
                heapq.heappop(ends)
            else:
                heapq.heappop(ends)
        return res

