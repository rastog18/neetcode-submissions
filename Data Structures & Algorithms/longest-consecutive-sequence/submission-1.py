class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can not use sort becuase it is O(n log n)
        # 1 - use adjacecny list - loop its keys for each key check if key+1 
        #     exists as a key if it does increase value count, return max value
        newSet = set()

        for i in nums:
            newSet.add(i)
        
        maxCount = 0
        for i in newSet:
            count = 1
            temp = i
            while temp + 1 in newSet:
                count += 1
                temp += 1
            maxCount = max(count, maxCount)
        return maxCount
        