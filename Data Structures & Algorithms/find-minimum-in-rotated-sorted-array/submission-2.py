class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while (l < r):
            toCheck = (l+r)//2
            if nums[toCheck] < nums[r]:
                r = toCheck
            else:
                l = toCheck + 1
        return nums[l]









        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     mid = (l+r)//2
        #     if nums[mid] < nums[r]:
        #         r = mid
        #     else:
        #         l = mid +1
        # return nums[l]

        