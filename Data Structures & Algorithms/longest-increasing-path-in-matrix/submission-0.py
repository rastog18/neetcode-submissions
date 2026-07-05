class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1 for i in range(m)] for j in range(n)]
        toRet = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            top = 1 + dfs(i-1, j) if i-1 >= 0 and matrix[i][j] < matrix[i-1][j] else 1
            bottom = 1 + dfs(i+1, j) if i+1 < n and matrix[i][j] < matrix[i+1][j] else 1
            left = 1 + dfs(i, j-1) if j-1 >= 0 and matrix[i][j] < matrix[i][j-1] else 1
            right = 1 + dfs(i, j+1) if j+1 < m and matrix[i][j] < matrix[i][j+1] else 1
            dp[i][j] = max(left, right, top, bottom)
            return dp[i][j]

        for i in range(n):
            for j in range(m):
                dfs(i,j)
                toRet = max(toRet,dp[i][j])

        return toRet