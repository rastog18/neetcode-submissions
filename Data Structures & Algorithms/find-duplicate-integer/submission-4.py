class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while(True):
            slow = nums[slow] # 1, 2
            fast = nums[nums[fast]] # 2, 3

            if slow == fast:
                break
        slow2 = 0
        while(True):
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow










        toReturn = 1
        for i in nums:
            # itm = abs(i)
            # print(itm)
            if nums[i-1] < 0:
                toReturn *= i
                break
            else:
                nums[i-1] *= -1
        print(nums)
        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         nums[i] *= -1
        return toReturn
        