class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        OPT = [[1 for j in range(n)] for i in range(m)]
        # total number of ways to reach the last box is #sum of its left + sum of its top

        for dig in range(1, m+n-1):
            for i in range(m):
                for j in range(n):
                    if i+j == dig:
                        if i-1 < 0:
                            OPT[i][j] = OPT[i][j-1] 
                        elif j-1 < 0:
                            OPT[i][j] = OPT[i-1][j]
                        else:
                            OPT[i][j] = OPT[i-1][j] + OPT[i][j-1]

        return OPT[m-1][n-1]
        