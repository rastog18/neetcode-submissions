class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()

        def addToQ(row, col, curDistance):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == -1:
                return
            if grid[row][col] < curDistance:
                return
            grid[row][col] = curDistance
            queue.append((row, col))
            

        def bfs():
            row, col = queue.popleft()

            distance = grid[row][col] + 1
            addToQ(row+1, col, distance)
            addToQ(row-1, col, distance)
            addToQ(row, col-1, distance)
            addToQ(row, col+1, distance)
           
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    addToQ(i,j, 0)
        while queue:
            bfs()