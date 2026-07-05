class Solution:

        
    def exist(self, board: List[List[str]], word: str) -> bool:

        path = set()

        def bt(i, j):

            if len(path) >= len(word):
                return True

            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or len(path) > len(word) or board[i][j] != word[len(path)]:
                return False
            
            res = False
            path.add((i,j))
            if (i, j+1) not in path:
                res = res or bt(i, j+1)
            if (i, j-1) not in path:
                res = res or bt(i, j-1)
            if (i-1, j) not in path:
                res = res or bt(i-1, j)
            if (i+1, j) not in path:
                res = res or bt(i+1, j)
            path.remove((i,j))
        
            return res
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = bt(i,j)
                if res:
                    return True

        return False
