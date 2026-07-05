class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        toReturn = 1
        for i in nums:
            itm = abs(i)
            if nums[itm-1] < 0:
                toReturn *= itm
                break
            else:
                nums[itm-1] *= -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
        return toReturn
        