class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        toRet = []
        subset = []

        def bt(i, total):
            if total == target:
                toRet.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            subset.append(nums[i])
            bt(i, total+nums[i])
            subset.pop()
            bt(i+1, total)
        bt(0, 0)
        return toRet
        