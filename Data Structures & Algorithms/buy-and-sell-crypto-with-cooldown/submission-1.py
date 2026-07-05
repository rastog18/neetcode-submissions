class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """At any given day 
            1) If Buying (no coin) I can Buy or Cooldown
            2) If Selling (1 coin) I can Sell or Cooldown
            3) Forced Cooldown after sell
        DP[n][buy/sell] - gives the maximum profit earned from day[n:]."""
        dp = {}
        n = len(prices)
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
    
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(cooldown, buy)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(cooldown, sell)
            
            return dp[(i, buying)]
        return dfs(0, True)
        