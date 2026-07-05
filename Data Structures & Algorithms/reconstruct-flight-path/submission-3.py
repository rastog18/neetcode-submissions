class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        neighbors = {}
        for _from, _to in sorted(tickets):
            if _from not in neighbors:
                neighbors[_from] = []
            neighbors[_from].append(_to)
        
        res = []

        def dfs(i):
            if i not in neighbors or len(neighbors[i]) == 0:
                res.append(i)
                return

            while len(neighbors[i]) > 0:
                n = neighbors[i].pop(0)
                dfs(n)
            res.append(i)

        dfs("JFK")
        res.reverse()
        return res