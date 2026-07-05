class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        toRet = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                toRet.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return toRet

        