class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        OPT = [False] * (n+1)
        OPT[0] = True

        for i in range(0, n):
            ind = i+1
            for w in wordDict:
                if ind - len(w) >= 0 and s[ind-len(w): ind] == w:
                    OPT[ind] = OPT[ind-len(w)]
                if OPT[ind] == True:
                    break
        return OPT[n]