"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # determine if all are non-overlapping intervals
        intervals.sort(key=lambda pair: pair.start)
        prevEnd = intervals[0].end if len(intervals) > 0 else 0
        for i in intervals[1:]:
            start = i.start
            end = i.end
            if prevEnd > start:
                return False
            prevEnd = end
        return True
