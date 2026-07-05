class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w2 = len(word2)
        w1 = len(word1)

        OPT = [[float("inf") for _ in range(w2 + 1)] for j in range(w1 + 1)]
        for j in range(w2+1):
            OPT[w1][j] = w2 - j
        for j in range(w1+1):
            OPT[j][w2] = w1 - j
        
        def dfs(i, j):
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                OPT[i][j] = dfs(i+1, j+1)
            else:
                OPT[i][j] = 1 + min(dfs(i+1, j+1), dfs(i+1, j), dfs(i, j+1))
            return OPT[i][j]

        return dfs(0,0)
                
            
        