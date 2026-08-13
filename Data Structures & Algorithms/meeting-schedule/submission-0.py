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
        print([(inter.start, inter.end) for inter in intervals])
        for interval in sorted_intervals:
            start = interval.start
            end = interval.end
            print(currTime)
            if currTime > start:
                return False
            currTime = end
        return True