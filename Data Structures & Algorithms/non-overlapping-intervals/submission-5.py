class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEnd = intervals[0][1]
        res = 0
        i = 1
        for start, end in intervals[1:]:
            # print(f"endV = {endV}, startN = {startN}")
            if prevEnd <= start:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res