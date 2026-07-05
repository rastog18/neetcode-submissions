class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)

        toRet = 0
        for i in range(k):
            toRet = heapq.heappop(heap)
        return toRet * -1
        