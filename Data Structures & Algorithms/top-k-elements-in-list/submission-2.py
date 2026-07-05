class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        adjList = {}
        for i in nums:
            adjList[i] = adjList.get(i, 0) + 1
        
        toRet = []
        heap_list = [(-value, key) for (key, value) in adjList.items()]
        heapq.heapify(heap_list) #sorts in ascending order
        for i in range(k):
            toRet.append(heapq.heappop(heap_list)[1])
        return toRet

        
    
    



        