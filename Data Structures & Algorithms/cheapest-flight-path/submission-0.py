class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = {}
        orderMap = {i : set() for i in range(n)}
        for (s, d, p) in flights:
            orderMap[s].add((d, p))

        def dfs(s, steps): # where ik is the number of steps
            if s == dst:
                return 0
            if steps > k:
                return float("inf")

            if (s, steps) in dp:
                return dp[(s, steps)]
            

            ans = float("inf")
            for (nei, dist) in orderMap[s]:
                    # direct = dist if nei == e else float("inf")
                    ans = min(dist + dfs(nei, steps+1), ans)
            dp[s, steps] = ans
            return dp[(s, steps)]

        
        res = dfs(src, 0)
        return -1 if res == float("inf") else res


            
            