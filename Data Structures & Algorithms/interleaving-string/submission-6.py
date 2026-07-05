class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        dp = {}

        def dfs(a, b):
            
            if a == len(s1) and b == len(s2):
                return True
            elif a+b >= len(s3):
                return False
            if (a,b) in dp:
                return dp[(a,b)]

            toRet = False
            i = a+b
            if a < len(s1) and s3[i] == s1[a]:
                toRet = toRet or  dfs(a+1, b)
            if b < len(s2) and s3[i] == s2[b]:
                toRet = toRet or dfs(a, b+1)
            dp[(a,b)] = toRet
            return dp[(a,b)]
        return dfs(0,0)