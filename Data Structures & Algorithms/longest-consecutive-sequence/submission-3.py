class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can not use sort becuase it is O(n log n)
        # 1 - use adjacecny list - loop its keys for each key check if key+1 
        #     exists as a key if it does increase value count, return max value
        # newSet = set()

        numSet = set(nums)
        maxLength = 0
        for i in numSet:
            if i-1 not in numSet:
                length = 1
                while length+i in numSet:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength
        # for i in nums:
        #     newSet.add(i)
        
        # maxCount = 0
        # for i in newSet:
        #     count = 1
        #     temp = i
        #     while temp + 1 in newSet:
        #         count += 1
        #         temp += 1
        #     maxCount = max(count, maxCount)
        # return maxCount

        # DP:
        # OPT = [1]* len(nums) # index -> maximum sequence
        # adjList = {} # number -> index
        # for i,j in enumerate(nums):
        #     prevIndex = adjList.get(j-1, -1)
        #     if prevIndex != -1:
        #         OPT[i] = OPT[prevIndex] + 1
        #     else:
        #         OPT[i] = 1
        #     adjList[j] = i
        # print(OPT)
        # return max(OPT)
        