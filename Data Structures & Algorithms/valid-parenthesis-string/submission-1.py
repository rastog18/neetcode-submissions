class Solution:
    def checkValidString(self, s: str) -> bool:
        i = 0
        opened = 0
        dp = {}

        def dfs(i, opened):
            if i >= len(s):
                return opened == 0
            if opened < 0:
                return False
            if (i, opened) in dp:
                return dp[(i, opened)]

            if s[i] == "(":
                dp[(i, opened)] = dfs(i+1, opened+1)
                return dp[(i, opened)]
            elif s[i] == ")":
                dp[(i, opened)] = dfs(i+1, opened-1)
                return dp[(i, opened)]
            else:
                takeL = dfs(i+1, opened+1)
                takeR = dfs(i+1, opened-1)
                skip = dfs(i+1, opened)
                dp[(i, opened)] = takeL or takeR or skip 
                return dp[(i, opened)]
        return dfs(0, opened)
            
        