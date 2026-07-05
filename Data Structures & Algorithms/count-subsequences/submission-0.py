class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(a, b):
            if b == len(t):
                return 1
            if a >= len(s):
                return 0
            if (a,b) in dp:
                return dp[(a,b)]

            take = dfs(a+1, b+1) if s[a] == t[b] else 0
            skip = dfs(a+1, b)

            dp[(a,b)] = take + skip
            return dp[(a,b)]

        return dfs(0,0)      