class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = {}
        orderMap = {}
        for (i,j,dist) in flights:
            if i not in orderMap:
                orderMap[i] = set()
            orderMap[i].add((j, dist))
        
        def dfs(i, stops):
            if i == dst:
                return 0

            if stops > k or i not in orderMap:
                return float("inf")

            if (i, stops) in dp:
                return dp[(i, stops)]

            ans = float("inf")
            for (nei, dist) in orderMap[i]:
                ans = min(ans, dfs(nei, stops+1) + dist)
            dp[(i, stops)] = ans
            return dp[(i, stops)]

        res = dfs(src, 0)
        return res if res != float("inf") else -1