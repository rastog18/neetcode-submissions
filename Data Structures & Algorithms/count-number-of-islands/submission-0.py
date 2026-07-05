class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate over all nodes which are not in visited
        # if 1:
            # itreate all possiblitities trying to find 1s
        toRet = 0
        visited = set()

        def bt(row, col):
            # print("visitinh at: ", end = "")
            # print(row, end= ", ")
            # print(col)
            if row >= len(grid) or col >= len(grid[0]) or col < 0 or row < 0:
                return
            
            if grid[row][col] == "0":
                return

            visited.add((row, col))
            if (row+1, col) not in visited:
                bt(row+1, col)
            if (row-1, col) not in visited:
                bt(row-1, col)
            if (row, col+1) not in visited:
                bt(row, col+1)
            if (row, col-1) not in visited:
                bt(row, col-1)
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                row = int(r)
                col = int(c)
                if (row, col) not in visited and grid[row][col] == "1":
                    # print("calling at: ", end = "")
                    # print(row, end= "")
                    # print(col)
                    toRet += 1
                    bt(row, col)
                    # print(visited)
        
        return toRet