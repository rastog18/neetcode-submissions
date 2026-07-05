class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        adjList = {}
        for i,j in enumerate(nums):
            adjList[j] = i
        print(adjList)
        for i,j in enumerate(nums):
            pos = adjList.get(target - j, -1)
            print(pos)
            if pos != -1 and i != pos:
                return [i, pos]
        return []