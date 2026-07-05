class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = set()
        time = 0
        def rot(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0 or grid[i][j] == 2:
                return

            grid[i][j] = 2
            fresh.remove((i,j))
            rotten.append((i,j))

        def freshToRot(i, j):
            rot(i+1, j)
            rot(i-1, j)
            rot(i, j+1)
            rot(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh.add((i,j))

        while rotten and len(fresh) != 0:
            # print(time, end=", rotten = ")
            # print(rotten, end=", ")
            # print(fresh)
            time += 1
            for i in range(len(rotten)):
                i, j = rotten.popleft()
                freshToRot(i, j)
                if len(fresh) == 0:
                    # print("broke here")
                    break
        if len(fresh) == 0:
            return time
        return -1
        