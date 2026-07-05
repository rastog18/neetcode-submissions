class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        startAndEnd = {}
        for i, j in enumerate(s):
            if startAndEnd.get(j) is None:
                startAndEnd[j] = 0
            startAndEnd[j] = i

        size, end = 0,0
        for i, j in enumerate(s):
            size += 1
            end = max(end, startAndEnd[j])

            if i == end:
                res.append(size)
                size = 0
        return res
