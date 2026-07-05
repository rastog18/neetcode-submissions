class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkForSimilarity(nums:List[str]) ->bool:
            tempAdjList = {}
            for i in nums:
                tempAdjList[i] = 1 + tempAdjList.get(i, 0)
                if (tempAdjList[i] > 1) and (i != "."):
                    return False
            return True

        for row in board:
            ret = checkForSimilarity(row)
            if (ret == False):
                return False
        
        for i in range(0, len(board)):
            col = []
            for j in range(0, len(board)):
                col.append(board[j][i])
            ret = checkForSimilarity(col)
            if (ret == False):
                return False
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                temp = board[i][j:j+3]
                temp += board[i+1][j:j+3]
                temp += board[i+2][j:j+3]

                ret = checkForSimilarity(temp)
                if (ret == False):
                    return False
        return True