class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monIncr = [[heights[0], 0]]
        spanSize = [[-1, -1] for _ in range(len(heights))]
        spanSize[0][0] = 0

        maxAr = heights[0]

        for i in range(1, len(heights)):
            if heights[i] > monIncr[-1][0]:     
                start = monIncr[-1][1] + 1
                spanSize[i][0] = start
                monIncr.append([heights[i],i])
            else:
                # Not monotonically increasing
                while monIncr and heights[i] <= monIncr[-1][0]:
                    popped = monIncr.pop()
                    spanSize[popped[1]][1] = i
                
                if monIncr:
                    start = monIncr[-1][1] + 1
                else: 
                    start = 0
                spanSize[i][0] = start
                monIncr.append([heights[i],i])
        # even now some of ends have not been updated.
        for i in range(len(spanSize)):
            if spanSize[i][1] == -1:
                spanSize[i][1] = len(heights)
            spanAr = (spanSize[i][1] - spanSize[i][0]) * heights[i]
            maxAr = max(spanAr, maxAr)
        return maxAr
        





        