class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        orderMap = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    orderMap[w1[j]].add(w2[j])
                    break
        
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True # in current Path
            for nei in orderMap[c]:
                if dfs(nei):
                    return True
            visit[c] = False # node is visited
            res.append(c)
        for c in orderMap:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)