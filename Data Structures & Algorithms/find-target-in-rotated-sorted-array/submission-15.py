class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left):
            l = minIndex
            r = len(nums)-1
            if left:
                l = 0
                r = minIndex-1
            while(l<=r):
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
            return -1
        #find the minimum
        l = 0
        r = len(nums)-1
        while (l < r):
            mid = (l+r)//2
            if nums[mid] <= nums[r]:
                r = mid
            else: #nums[mid] > nums[r]
                l = mid + 1
        minIndex = l
        print(minIndex)

        # do another pass binary search
        if nums[minIndex] <= target and target <= nums[-1]:
            # ibnary search on nums[minIndex:-1]
            return binarySearch(False)
        else:
            # binary search on nums[0:minIndex]
            return binarySearch(True)
        
        # middle calculate karo if that is target return
        # if middle < nums[r] and middle < target then l = mid + 1
        # if middle < nums[r] and middle > target then r = mid
        # if middle > nums[r] and middle < target = then r = mid
        # else l = mid + 1
        
        # I do not think this is the way, one approach to do it definaletly would be 
        # to find the minimum and make a new array from the min, and find the target there

        # real way : find the minimum using binary aearch, and from they do two binary searches
        # both on ascending lists

        # l = 0
        # r = len(nums) - 1

        # while(l < r):
        #     mid = (l+r)//2
        #     if (nums[mid] <= nums[r]):
        #         r = mid
        #     else:
        #         l = mid + 1
        # if l > 0 and nums[0] <= target and target <= nums[l-1]:
        #     L = 0
        #     R = l-1
        # else:
        #     L = l
        #     R = len(nums)-1
        # while(L <= R):
        #     mid = (L+R)//2
        #     if (nums[mid] == target):
        #         return mid
        #     elif (nums[mid] < target):
        #         L = mid + 1
        #     else:
        #         R = mid - 1
        
        # return -1

