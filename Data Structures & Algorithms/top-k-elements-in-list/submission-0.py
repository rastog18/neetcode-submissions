class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # crearte an adjlist
        # create a heap

        adjList = {}
        for i in nums:
            adjList[i] = 1 + adjList.get(i, 0)
        
        toReturn = dict(sorted(adjList.items(), key=lambda item: item[1]))
        keys = list(toReturn.keys())
        len_ = len(keys)
        return keys[len_ - k: len_]




        