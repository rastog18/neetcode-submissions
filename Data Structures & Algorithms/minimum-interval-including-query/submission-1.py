class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        maxEndTime = max(interval[1] for interval in intervals)
        minInterval = [float("inf") for i in range(maxEndTime+1)]

        for i in range(len(intervals)):
            curLen = intervals[i][1] - intervals[i][0] + 1
            for j in range(intervals[i][0], intervals[i][1]+1):
                minInterval[j] = min(minInterval[j], curLen)
        res = []
        for j in queries:
            if j > maxEndTime or minInterval[j] == float("inf"):
                res.append(-1)
            else:
                res.append(minInterval[j])
        return res



        