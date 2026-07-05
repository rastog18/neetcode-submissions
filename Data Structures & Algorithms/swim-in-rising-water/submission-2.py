class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], 0, 0))
        visited = set()

        while(minHeap):
            peak, i, j = heapq.heappop(minHeap)
            visited.add((i,j))
            # print(f"peak = {peak}, i = {i}, j = {j}")
            if i == len(grid)-1 and j == len(grid[0]) - 1:
                return peak

            if 0 <= i-1 and (i-1, j) not in visited:
                newPeak = max(peak, grid[i-1][j])
                # print(f"adding: {newPeak}")
                heapq.heappush(minHeap, (newPeak, i-1, j))

            if i+1 < len(grid) and (i+1, j) not in visited:
                newPeak = max(peak, grid[i+1][j])
                # print(f"adding: {newPeak}")
                heapq.heappush(minHeap, (newPeak, i+1, j))
            if j+1 < len(grid[0]) and (i, j+1) not in visited:
                newPeak = max(peak, grid[i][j+1])
                # print(f"adding: {newPeak}")
                heapq.heappush(minHeap, (newPeak, i, j+1))
            if 0 <= j-1 and (i, j-1) not in visited:
                newPeak = max(peak, grid[i][j-1])
                # print(f"adding: {newPeak}")
                heapq.heappush(minHeap, (newPeak, i, j-1))
