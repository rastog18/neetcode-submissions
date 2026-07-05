class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dictOut = {}
        neighbors = {}
        tickets.sort()
        for _from, _to in tickets:
            if _from not in dictOut:
                dictOut[_from] = 0
                neighbors[_from] = []
            dictOut[_from] += 1
            neighbors[_from].append(_to)
        
        res = []

        def dfs(i):
            if i not in dictOut or dictOut[i] == 0:
                res.append(i)
                return

            while len(neighbors[i]) > 0:
                n = neighbors[i].pop(0)
                dictOut[i] -= 1
                dfs(n)
            res.append(i)

        dfs("JFK")
        res.reverse()
        return res