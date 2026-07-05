class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each index in row | col | sqr represents bitmap of 
        # the row | col | sqr
        n = len(board)
        row = [0] * n
        col = [0] * n
        sqr = [0] * n

        for i in range(0,n):
            for j in range(0, n):
            
                num = board[i][j]
                if (num == "."):
                    continue
                else:
                    val = int(num)

                    # we can compare bitmaps to each other - we open the bitmap 
                    # ar row[i] and check if the 1 >> val position is filled
                    if (1 << val) & row[i]:
                        print(1)
                        return False
                    if (1 << val) & col[j]:
                        print(2)
                        return False
                    if (1 << val) & sqr[(i//3)*3 + j//3]:
                        print(3)
                        return False
                    
                    row[i] |= 1 << val
                    col[j] |= 1 << val
                    sqr[i//3 + j//3] |= 1 << val
        return True
                    
