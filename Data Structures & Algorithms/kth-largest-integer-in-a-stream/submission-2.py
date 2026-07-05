from heapq import heappop, heappush, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.lenMax = k
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)


    def add(self, val: int) -> int:
        if len(self.heap) < self.lenMax:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)
        return self.heap[0]

