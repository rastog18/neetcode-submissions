class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subsets = []
        aim = sum(nums)/2

        for i in nums:
            # add i to all subsets, even as an individual
            for j in range(len(subsets)):
                newSet = subsets[j].copy()
                newSet.append(i)
                subsets.append(newSet)
            subsets.append([i])
        
        for i in subsets:
            if sum(i) == aim:
                return True
        return False

        