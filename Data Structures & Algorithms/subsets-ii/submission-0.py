class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        toRet = []
        subset = []

        def bt(i):
            if i >= len(nums):
                toRet.append(subset.copy())
                return
            subset.append(nums[i])
            bt(i+1)
            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i+=1
            subset.pop()
            bt(i+1)
        
        bt(0)
        return toRet
        