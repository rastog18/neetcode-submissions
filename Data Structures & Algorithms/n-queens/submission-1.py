class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colOccupied = set()
        ldagOccupied = set()
        udagOccupied = set()
        # rowOccupied = set()

        def canPlaceQueen(i, j):
            if (i-j not in ldagOccupied and i+j not in udagOccupied and j not in colOccupied):
                return True
            return False

        toRet = []
        pos = []
        for m in range(n):
            row = ""
            for p in range(n):
                if m == p:
                    row += "Q"
                else:
                    row += "."
            pos.append(row)
        board = []
        def bt(i):
            if i >= n:
                toRet.append(board.copy())
                return
            for j in range(n):
                if canPlaceQueen(i,j):
                    colOccupied.add(j)
                    # rowOccupied.add(i)
                    ldagOccupied.add(i-j)
                    udagOccupied.add(i+j)
                    board.append(pos[j])
                    bt(i+1)
                    board.pop()
                    colOccupied.remove(j)
                    # rowOccupied.remove(i)
                    ldagOccupied.remove(i-j)
                    udagOccupied.remove(i+j)

        bt(0)
        return toRet

        