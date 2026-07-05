class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for cords in points:
            distance = cords[0]**2 + cords[1]**2
            heapq.heappush(heap, (distance, cords))
        
        toRet = []
        for i in range(k):
            toRet.append(heapq.heappop(heap)[1])
        return toRet

        