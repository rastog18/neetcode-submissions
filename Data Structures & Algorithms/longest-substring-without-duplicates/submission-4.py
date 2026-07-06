class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        adjList = {} #char -> index
        l = 0
        for i,j in enumerate(s):
            moveLTo = adjList.get(j, -1)+1
            if moveLTo != -1 and moveLTo > l:
                l = moveLTo
            adjList[j] = i
            res = max(res, i - l +1)
        return res

        #     if i in sldWindow:
        #         lenString = max(lenString, len(sldWindow))
        #         fromIndex = sldWindow.index(i) + 1
        #         sldWindow = sldWindow[fromIndex:]

        #     sldWindow.append(i)
        # return max(lenString, len(sldWindow))
        