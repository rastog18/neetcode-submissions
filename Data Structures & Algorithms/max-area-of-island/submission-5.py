class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()

        def count(i, j, area):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
                return area

            visited.add((i,j))

            l =  count(i+1, j, area)
            r =  count(i-1, j, area)
            u =  count(i, j-1, area)
            d =  count(i, j+1, area)

            return l + r + u + d + 1
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = count(i,j, 0)

                    maxArea = max(maxArea, area)
        return maxArea