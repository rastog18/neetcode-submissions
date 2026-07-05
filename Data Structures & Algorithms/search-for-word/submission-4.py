class Solution:
    def __init__(self):
        self.found = False
        
    def exist(self, board: List[List[str]], word: str) -> bool:

        path = set()
        
        # iterate over all nodes

        def bt(i, j):

            if len(path) >= len(word):
                self.found = True
                return

            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return
            
            
            k = len(path)
            if len(path) < len(word) and board[i][j] == word[k]:
                path.add((i,j))
                if (i, j+1) not in path:
                    bt(i, j+1)
                if (i, j-1) not in path:
                    bt(i, j-1)
                if (i-1, j) not in path:
                    bt(i-1, j)
                if (i+1, j) not in path:
                    bt(i+1, j)
                path.remove((i,j))
    
            if len(path) == 0:
                if j >= len(board[0])-1:
                    j = 0
                    i += 1
                else:
                    j+=1
    
                bt(i, j)

        bt(0,0)
        return self.found
