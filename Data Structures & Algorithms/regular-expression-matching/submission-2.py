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

            next_r = p[r+1] if r+1 < len(p) else None
            rC = p[r]
            lC = s[l] if l+1 <= len(s) else None

            if next_r == "*":
                take = l < len(s) and (rC == "." or rC == s[l]) and dfs(l+1, r)
                skip = dfs(l, r+2)
                dp[(l,r)] = take or skip
                return dp[(l,r)]
            else:
                dp[(l,r)] =  (lC == rC or rC == ".") and dfs(l+1, r+1)
                return dp[(l, r)]


        return dfs(0,0)

