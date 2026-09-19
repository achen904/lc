"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            a1 = intervals[i-1].start
            b1 = intervals[i-1].end
            a2 = intervals[i].start
            if a1 <= a2 < b1:
                return False
        return True