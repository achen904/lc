class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        seen = set()
        def isValid(x,y):
            if not 0 <= x < len(board):
                return False
            if not 0 <= y < len(board[0]):
                return False
            if board[x][y] == "O":
                return True

        def dfs(x,y):
            seen.add((x,y))
            for dx, dy in directions:
                nxt = (x + dx, y + dy)
                if nxt not in seen and isValid(x + dx, y + dy):
                    dfs(x + dx, y + dy)
        #traverse the edges and find the 0s, and run dfs on them
        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                dfs(i, len(board[0]) - 1)
        for i in range(len(board[0])):
            if board[0][i] == "O":
                dfs(0, i)
            if board[len(board) - 1][i] == "O":
                dfs(len(board) - 1, i)
        #traverse the board to see if the "0" is reached from an outside 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                index = (i,j)
                if board[i][j] == "O" and index not in seen:
                    board[i][j] = "X"

        