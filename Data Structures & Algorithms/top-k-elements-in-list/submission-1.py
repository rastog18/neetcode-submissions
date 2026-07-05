import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        adjList = {}
        for i in nums:
            adjList[i] = adjList.get(i,0) + 1
        
        toRet = []
        heap_list = [(-1*value, key) for key,value in adjList.items()]
        heapq.heapify(heap_list)
        for i in range(k):
            add = heapq.heappop(heap_list)
            toRet.append(add[1])
        return toRet

    
    



        