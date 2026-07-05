class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        OPT[][] returns the fewest number of coins required to sum up the amount
        OPT [n][amt] = min {
            1 + OPT[n][amt-coins[n]]
            OPT[n-1][amt]
        }
        Base Case: OPT[n][amt] if coins[n] > amt OPT[n][amt] = -1
        OPT[n][n] = 1
        """

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(1 + dp[amt - c], dp[amt])
        return -1 if dp[amount] == float("inf") else  dp[amount] 
        


        


        