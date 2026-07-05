class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        lRows = len(matrix)
        lCols = len(matrix[0])

        l = 0
        r = lRows
        toCheck = (r+l) // 2

        while(l <  r):
            if (matrix[toCheck][0] <= target and target <= matrix[toCheck][lCols-1]):
                row = toCheck
                break
            elif (target < matrix[toCheck][0]):
                r = toCheck
            else:
                l = toCheck + 1
            toCheck = (r+l)//2
        
        # now that we have the row in which we want to find the element find, we perform
        # binary search again
        l = 0
        r = lCols

        toCheck = (r+l) // 2
        while(l <  r):
            if (matrix[row][toCheck] == target):
                return True
            elif (matrix[row][toCheck] < target):
                l = toCheck + 1
            else:
                r = toCheck
            toCheck = (r+l)//2
        return False
        