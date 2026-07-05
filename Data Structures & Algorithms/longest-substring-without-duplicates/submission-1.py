class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sldWindow = []
        lenString = 0
        for i in s:
            if i in sldWindow:
                lenString = max(lenString, len(sldWindow))
                fromIndex = sldWindow.index(i) + 1
                sldWindow = sldWindow[fromIndex:]

            sldWindow.append(i)
        return max(lenString, len(sldWindow))
        