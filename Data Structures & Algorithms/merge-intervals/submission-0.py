class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newInterval = []
        res = []

        for i in range(len(intervals)):
            curI = newInterval if len(newInterval) > 0 else intervals[i]
            nextI = intervals[i+1] if i+1 < len(intervals) else [float("inf"), float("inf")]

            if curI[1] < nextI[0]:
                res.append(curI)
                newInterval = []
            else:
                newInterval = [min(curI[0], nextI[0]), max(curI[1], nextI[1])]
        return res
        