class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # IF WE ENCOUNTER . increment both l and r
        # if we encounter a '*' increment only l till the l != prev_r
        # in case of a normal letter if they do not match we return a F
        dp = {}
        def dfs(l, r):
            if (l,r) in dp:
                return dp[(l,r)]

            if r == len(p):
                return l == len(s)

            match = l < len(s) and (s[l] == p[r] or p[r] == ".")

            if r+1 < len(p) and p[r+1] == "*":
                dp[(l,r)] = dfs(l, r+2) or (match and dfs(l+1, r))
                return dp[(l,r)]
            else:
                dp[(l,r)] = match and dfs(l+1, r+1)
                return dp[(l,r)]


        return dfs(0,0)

