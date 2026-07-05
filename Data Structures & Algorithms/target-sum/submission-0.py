class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(target, i):
            if target == 0 and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            if (target, i) in dp:
                return dp[(target, i)]
            
            neg = dfs(target + nums[i], i+1)
            pos = dfs(target - nums[i], i+1)
            dp[(target, i)] = neg + pos
            return dp[(target, i)]
        return dfs(target, 0)
        