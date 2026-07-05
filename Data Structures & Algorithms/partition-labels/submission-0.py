class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        startAndEnd = {}
        for i, j in enumerate(s):
            if startAndEnd.get(j) is None:
                startAndEnd[j] = [i, i]
            startAndEnd[j][1] = i

        i = 0
        while i < len(s):
            j, farthest = i, startAndEnd[s[i]][1]
            while j <= farthest:
                farthest = max(farthest, startAndEnd[s[j]][1])
                j += 1
            res.append(farthest-i+1)
            i = farthest + 1
        return res