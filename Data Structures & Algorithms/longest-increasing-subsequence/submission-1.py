class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        OPT = [1] * n
        for i in range(1, n):
            curNum = nums[i]
            # find the numer before ith index with value less than nums[i]
            for j in range(i, -1, -1):
                toCheck = nums[j]
                if toCheck < curNum:
                    OPT[i] = max(OPT[j] + 1, OPT[i])
        print(OPT) 
        return max(OPT)