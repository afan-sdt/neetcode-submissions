"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        count, s, e , res = 0, 0, 0, 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                count +=1
                res = max(count, res)
                s+=1
            else:
                e+=1
                count -=1
        return res