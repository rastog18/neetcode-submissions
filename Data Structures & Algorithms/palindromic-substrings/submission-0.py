class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        OPT = [[0] * n for i in range(n)]

        count = 0
        
        # base case
        for i in range(n):
            OPT[i][i] = 1
            count += 1
            if i < n-1 and s[i] == s[i+1]:
                count += 1
                OPT[i][i+1] = 1
        
        # recurrnace relation
        for length in range(3, n+1):
            for i in range(n-length+1):
                start = i
                end = i + length - 1
                if s[start] == s[end] and OPT[start+1][end-1] == 1:
                    OPT[start][end] = 1
                    count += 1
                else:
                    OPT[start][end] = 0
    
        return count
        