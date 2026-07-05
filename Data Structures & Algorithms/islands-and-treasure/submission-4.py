class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        distance = 0

        def addToQueue(i,j, distance):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return
            if grid[i][j] == -1:
                return
            if distance > grid[i][j]:
                return
            grid[i][j] = distance
            q.append((i,j))
            # visited.append((i,j))

        def distanceToTreasure():
            i,j = q.popleft()
            distance = grid[i][j]
               
            distance += 1
            addToQueue (i+1, j, distance)
            addToQueue(i-1, j, distance)
            addToQueue(i, j+1, distance)
            addToQueue(i, j-1, distance)
                
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0: # only call the function on treasures
                    addToQueue(i,j,0)
        while q:
            distanceToTreasure()