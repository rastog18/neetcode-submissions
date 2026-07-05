class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = [-i for i in stones]
        heapq.heapify(heap)
        while(len(heap) > 1):
            a = -1 * heapq.heappop(heap)
            b = -1 * heapq.heappop(heap)

            if (a == b):
                heapq.heappush(heap, 0)
            else:
                insert = -1 * abs(a-b)
                heapq.heappush(heap, insert)
        return -1* heap[0]


        