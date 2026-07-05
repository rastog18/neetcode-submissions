class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        OPT = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                top = OPT[i-1][j] if i-1 >= 0 else 0
                bottom = OPT[i][j-1] if j-1 >= 0 else 0
                dig = OPT[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                case1 = 1 + dig if text1[j] == text2[i] else 0
                OPT[i][j] = max(case1, top, bottom)

        return OPT[n-1][m-1]
        