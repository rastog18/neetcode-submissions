class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # for every O check for adjacent Xs
        # if you encounter a O instead add that to visitNext queue, if not is visited
        # if the visit next queue is empty and change all nodes in sorrounded to X
        # skip the visited nodes
        ROWS, COLS = len(board), len(board[0])
        sorroundedNodes = set()
        visitedNodes = set()
        visitNext = deque()

        def isSorrounded(i, j):
            if i == 4 and j == 8:
                print("executing")
                print(visitedNodes)
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False
            if (i,j) in visitedNodes:
                return True
            if board[i][j] == "X":
                return True

            visitedNodes.add((i,j))
            sorroundedNodes.add((i,j))

            right = isSorrounded(i+1, j)
            left = isSorrounded(i-1, j)
            down = isSorrounded(i, j+1) 
            up = isSorrounded(i, j-1)

            return right and left and down and up

        for i in range(ROWS):
            for j in range(COLS):
                print(i, end = ", j= ")
                print(j)
                # if i == 4 and j == 8:
                #     print("hello")
                #     print(visitedNodes)
                if board[i][j] == "O" and (i,j) not in visitedNodes:
                    sorroundedNodes.clear()
                    toFill = isSorrounded(i, j)
                    if toFill:
                        for m,n in sorroundedNodes:
                            board[m][n] = "X"


        