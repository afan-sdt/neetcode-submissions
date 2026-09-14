"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for i in intervals:
            times.append([i.start, 1])
            times.append([i.end, -1])
        times.sort()
        count = 0
        res = 0
        for t in times:
            count += t[1]
            res = max(res, count)
        return res