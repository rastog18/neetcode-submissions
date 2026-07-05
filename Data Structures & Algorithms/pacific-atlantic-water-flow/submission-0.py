class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if the passed node is true return true other wise check for node
        # checking for node
            # check at left, right, up, down
        ROWS, COLS = len(heights)-1, len(heights[0])-1
        waterToPacific = set()
        waterToAtlantic = set()
        toRet = []

        def canReachOcean(i, j, prev, ocean):
            if i > ROWS or j > COLS or i < 0 or j < 0 or heights[i][j] < prev:
                return

            if ocean == 1:
                if (i,j) in waterToPacific:
                    return
                waterToPacific.add((i,j))
                if (i, j) in waterToAtlantic:
                    toRet.append([i,j])

            if ocean == 2:
                if i == 0 and j == 3:
                    print
                if (i,j) in waterToAtlantic:
                    return
                waterToAtlantic.add((i,j))
                if (i, j) in waterToPacific:
                    toRet.append([i,j])

            prev = heights[i][j]

            canReachOcean(i+1, j, prev, ocean)
            canReachOcean(i-1, j, prev, ocean)
            canReachOcean(i, j+1, prev, ocean)
            canReachOcean(i, j-1, prev, ocean)

        for i in range(0, ROWS+1):
            for j in range(0, COLS+1):
                if i == 0 or j == 0:
                    canReachOcean(i, j, -float('inf'), 1)
                if i == ROWS or j == COLS:
                    canReachOcean(i, j, -float('inf'), 2)
        return toRet