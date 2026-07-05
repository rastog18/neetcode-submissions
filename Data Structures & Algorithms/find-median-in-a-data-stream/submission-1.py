class MedianFinder:

    def __init__(self):
        self.minHeap = [] # the right heap
        self.maxHeap = [] # the left heap

        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if self.maxHeap == []:
            heapq.heappush(self.maxHeap, -1*num)
            return
        maxVal = -1 * self.maxHeap[0]
        if num > maxVal:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1*num)
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                element = -1 * heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, element)
            else:
                element = -1 * heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, element)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-1 * self.maxHeap[0])) /2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -1 * self.maxHeap[0]
        