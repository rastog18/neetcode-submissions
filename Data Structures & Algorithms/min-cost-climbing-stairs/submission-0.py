class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        OPT = [0] * (n+1)

        for i in range(2, n+1):
            OPT[i] = min(cost[i-1] + OPT[i-1], 
            cost[i-2] + OPT[i-2])
        return OPT[n]            