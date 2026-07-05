class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        OPT = [0] * (n+1)
        OPT[1] = nums[0]

        for i in range(2, n+1):
            OPT[i] = max(OPT[i-1], OPT[i-2] + nums[i-1])
        print(OPT)
        return OPT[n]
        