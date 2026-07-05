class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        OPT = [1] * (n+1)
        LN = [1] * (n+1)

        for i in range(1, n+1):
            num = nums[i-1]

            num1 = OPT[i-1] * num
            num2 = LN[i-1] * num

            OPT[i] = max(num1, num2, num)
            LN[i] = min(num1, num2, num)

        return max(max(OPT[1:]), max(LN[1:]))