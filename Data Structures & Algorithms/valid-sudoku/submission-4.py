class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row using hashMap
        # check col using hashMap
        
        def checkDuplicate(toCheck:List[str]) ->bool:
            adjList = {}
            for i in toCheck:
                if i != ".":
                    adjList[i] = adjList.get(i, 0) + 1
                    if adjList[i] == 2:
                        return True
            return False
        
        for i in range(0, 9):
            row = []
            col = []
            for j in range(0,9):
                rowLine = board[i][j]
                colLine = board[j][i]
                row.append(rowLine)
                col.append(colLine)
            if checkDuplicate(row) or checkDuplicate(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if checkDuplicate(temp):
                    return False
        return True



                    
