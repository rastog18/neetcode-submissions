class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        coins.sort()

        def dfs(amt, i):
            if amt == 0:
                return 1
            if i >= len(coins) or amt <= 0:
                return 0

            if (amt,i) in dp:
                return dp[(amt, i)]

            take = dfs(amt - coins[i], i)
            skip = dfs(amt, i+1)
            dp[(amt, i)] = take + skip

            return dp[(amt, i)]
        return dfs(amount,0)

        