class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        OPT = [[0] * n for i in range(n)]

        maxSubstr = s[0]
        maxLen = 1
        
        # base case
        for i in range(n):
            OPT[i][i] = 1
            if i < n-1 and s[i] == s[i+1]:
                maxLen = 2
                maxSubstr = s[i:i+2]
                OPT[i][i+1] = 1
        
        # recurrnace relation
        for length in range(3, n+1):
            for i in range(n-length+1):
                start = i
                end = i + length - 1
                if s[start] == s[end] and OPT[start+1][end-1] == 1:
                    OPT[start][end] = 1
                    if end - start + 1 > maxLen:
                        maxLen = end - start + 1
                        maxSubstr = s[start:end+1]
                else:
                    OPT[start][end] = 0
        
        # indentification of longest substring
        
        for i in range(n):
            for j in range(n):
                if j > i and OPT[i][j] == 1:
                    curLen = j - i + 1
                    if curLen > maxLen:
                        maxLen = curLen
                        maxSubstr = s[i:j+1]
        return maxSubstr