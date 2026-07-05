class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Direct dfs is not worth it becasue we end up counting permutations instead of combinations
        dp = {}
        coins.sort()

        def dfs(amount, i):
            if amount == 0:
                return 1
            if amount < 0 or i < 0 or i >= len(coins):
                return 0
            if (amount, i) in dp:
                return dp[(amount, i)]

            take = dfs(amount - coins[i], i)
            skip = dfs(amount , i+1)
            dp[(amount, i)] = take + skip

            return dp[(amount, i)]
        return dfs(amount, 0)
        