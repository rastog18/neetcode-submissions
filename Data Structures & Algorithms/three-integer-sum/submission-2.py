class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # skip the numbers you have already visisted
        # follow two pointer approach for the rest

        def twoSum(index, num) -> List[List[int]]:
            target = 0 - num
            l = index + 1
            r = len(nums) - 1
            toReturn = []
            while(l < r):
                if (nums[l] + nums[r] < target):
                    l += 1
                elif (nums[l] + nums[r] > target):
                    r -= 1
                else:
                    curL = nums[l]
                    curR = nums[r]
                    toReturn.append([num, curL, curR])
        
                    l+=1
                    while(l < len(nums) and nums[l] == curL):
                        l+=1
                    r -= 1
                    while(0 <= r and nums[r] == curR):
                        r -= 1
            return toReturn

        toReturn = []
        nums.sort()
        for i,j in enumerate(nums):
            if (i != 0 and nums[i] == nums[i-1]):
                continue
            temp = twoSum(i,j)
            toReturn += temp
        return toReturn
