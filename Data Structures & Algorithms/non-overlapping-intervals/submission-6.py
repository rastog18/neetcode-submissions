class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort in increasing order
        # if the prevEnd >= curStart : overlap
            # res += 1
            # prevEnd = min(prevEnd, curStart)
        # else:
            # update prevEnd
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            # print(f"privEnd = {prevEnd}, start = {start}")
            if prevEnd > start:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return res