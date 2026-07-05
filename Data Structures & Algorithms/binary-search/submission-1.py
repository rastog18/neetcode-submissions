class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [a, b, c, d] -> c and [a,b,c] -> b

        l = 0
        r = len(nums)
        toCheck = (r+l)//2
        while(l <= toCheck and toCheck < r):
            if nums[toCheck] == target:
                return toCheck
            elif nums[toCheck] < target:
                # update l
                l = toCheck + 1
            else:
                # update r
                r = toCheck
            toCheck = (r+l)//2
        return -1

        