class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            temp = 0
            for i in range(l, r+1):
                temp2 = dfs(l, i-1) + dfs(i+1, r) + nums[l-1] * nums[i] * nums[r+1]
                temp = max(temp, temp2)
            return temp
        return dfs(0+1, len(nums)-2)
        