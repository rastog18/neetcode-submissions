class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def dfs(a, b, i):
            if i == len(s3) and a == len(s1) and b == len(s2):
                return True
            elif i >= len(s3):
                return False
            if (a,b) in dp:
                return dp[(a,b)]

            toRet = False
            if a < len(s1) and s3[i] == s1[a]:
                toRet = toRet or  dfs(a+1, b, i+1)
            if b < len(s2) and s3[i] == s2[b]:
                toRet = toRet or dfs(a, b+1, i+1)
            dp[(a,b)] = toRet
            return dp[(a,b)]
        return dfs(0,0,0)