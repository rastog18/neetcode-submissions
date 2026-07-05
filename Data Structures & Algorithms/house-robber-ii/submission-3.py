
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 1:
            return nums[0]
        nums1 = nums[0: n-1]
        nums2 = nums[1: n]

        OPT1 = [0] * n
        OPT2 = [0] * n

        OPT1[1] = nums1[0]
        OPT2[1] = nums2[0]

        for i in range(2, n):
            OPT1[i] = max(OPT1[i - 1], OPT1[i - 2] + nums1[i - 1])
            OPT2[i] = max(OPT2[i - 1], OPT2[i - 2] + nums2[i - 1])

        return max(OPT1[n-1], OPT2[n-1])
