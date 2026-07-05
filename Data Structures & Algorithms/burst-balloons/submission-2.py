class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        OPT = {}
        nums = [1] + nums + [1]

        def burst(l,r):
            if l > r:
                return 0
            # if l == r, this means that only one balloon is left
            if (l, r) in OPT:
                return OPT[(l,r)]

            OPT[(l,r)] = -float("inf")
            for i in range(l, r+1):
                OPT[(l,r)] = max(OPT[(l,r)], burst(l, i-1) + burst(i+1, r) + nums[i] * nums[l-1] * nums[r+1])
            return OPT[(l,r)]
            
        return burst(0+1, len(nums)-2)

        # at every baloon we get three options:
            # skip
        