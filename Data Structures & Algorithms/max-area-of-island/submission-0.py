class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()

        def bt(row, col, curArea):
            print(row, end = ", ")
            print(col, end = ", ")
            print(curArea)
            if row >= len(grid) or col >= len(grid[0]) or col < 0 or row < 0:
                return curArea
            
            if grid[row][col] == 0:
                return curArea

            visited.add((row, col))
            left,right,up,down = 0,0,0,0
            if (row+1, col) not in visited:
                right = bt(row+1, col, curArea)
            if (row-1, col) not in visited:
                left = bt(row-1, col, curArea)
            if (row, col+1) not in visited:
                up = bt(row, col+1, curArea)
            if (row, col-1) not in visited:
                down = bt(row, col-1, curArea)
            return 1 + left + right + up + down
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                row = int(r)
                col = int(c)
                if (row, col) not in visited and grid[row][col] == 1:
                    curArea = bt(row, col, 0)
                    maxArea = max(maxArea, curArea)
        
        return maxArea
        