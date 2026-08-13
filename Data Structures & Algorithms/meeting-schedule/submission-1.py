"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda inter: (inter.start, inter.end))
        currTime = -1
        for interval in sorted_intervals:
            start = interval.start
            end = interval.end
            if currTime > start:
                return False
            currTime = end
        return True