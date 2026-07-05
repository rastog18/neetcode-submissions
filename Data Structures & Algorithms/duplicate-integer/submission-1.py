class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # 1 we could add to the index if is one alreay return true
        """
        sNums = len(nums)
        newList = [0*sNums]
        for i in nums:
            if (newList[i%sNums] != 0):
                return true
            newList[i%sNums] += 1
         return true
         # but this solution will only work if we have consecutive numbers """
        """
        for i in range(0, len(nums)-1):
            if (nums[i]== nums[i+1]):
                return True
        return False
        # but this will only work if it is sorted
        """

        # we have to make an adjacency list
        adjList = {}
        for i in nums:
            adjList[i] = 0
        for i in nums:
            adjList[i] += 1
            if (adjList[i] == 2):
                return True
        return False