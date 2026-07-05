class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()

        def distanceToTreasure(i, j, distance):
            # print("i = ", end = "")
            # print(i, end=",j = ")
            # print(j, end =", dist = ")
            # print(distance)
            # print(visited)
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                # print("return")
                return
            if grid[i][j] == -1:
                # print("return")
                return
            if distance > grid[i][j]:
                print(distance)
                print(grid[i][j])
                return
            visited.add((i,j))
            if i+1 < len(grid) and (i+1, j) not in visited: # goDown
                grid[i+1][j] = min(distance+1, grid[i+1][j])
                # print("going down")
                distanceToTreasure(i+1, j, distance+1)
                

            if i-1 >= 0 and (i-1, j) not in visited:         # goUp
                grid[i-1][j] = min(distance+1, grid[i-1][j])
                # print("going up")
                distanceToTreasure(i-1, j, distance+1)
                

            if j+1 < len(grid[0]) and (i, j+1) not in visited: #goRight
                grid[i][j+1] = min(distance+1, grid[i][j+1])
                # print("going right")
                distanceToTreasure(i, j+1, distance+1)
                

            if j-1 >= 0 and (i, j-1) not in visited: #goLeft
                grid[i][j-1] = min(distance+1, grid[i][j-1])
                # print("going left")
                distanceToTreasure(i, j-1, distance+1)
                
            visited.remove((i,j))
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0: # only call the function on treasures
                    # print("calling")
                    distanceToTreasure(i, j, 0)