"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda pair : pair.start)
        if len(intervals) <= 0:
            return 0

        maxEndTime = max(interval.end for interval in intervals)
        meetingTimes = [0 for i in range(maxEndTime)]

        for i in range(len(intervals)):
            for j in range(intervals[i].start, intervals[i].end):
                meetingTimes[j] += 1
        return max(meetingTimes)


