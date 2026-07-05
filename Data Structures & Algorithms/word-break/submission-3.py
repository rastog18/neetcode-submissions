class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        OPT = [False] * (n+1)
        OPT[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and s[i : i+len(w)] == w:
                    OPT[i] = OPT[i+len(w)]
                if OPT[i] == True:
                    break
        return OPT[0]