class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        toReach = n - 1
        for i in range(n-2, -1, -1):
            if nums[i] - (toReach - i) >= 0:
                toReach = i
        return True if toReach == 0 else False
        