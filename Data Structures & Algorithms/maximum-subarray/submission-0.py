class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in range(0, len(nums)):
            curSum += nums[n]
            maxSum = max(curSum, maxSum)
            curSum = 0 if curSum < 0 else curSum
        return maxSum
        