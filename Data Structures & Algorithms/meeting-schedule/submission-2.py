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

        for i in range(1, len(intervals)):
            prevEnd = intervals[i-1].end
            curstart = intervals[i].start

            if prevEnd > curstart:
                return False

        return True
