class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        toRet = []

        def dfs(total, i, subset):
            if total == target:
                toRet.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(total + nums[i], i, subset)
            subset.pop()
            dfs(total, i+1, subset)

        dfs(0, 0, [])
        return toRet
        