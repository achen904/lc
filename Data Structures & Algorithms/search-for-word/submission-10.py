class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Run DFS on an occurence of the first character in word
        #mark visited cells as # so we don't revisit
        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        def dfs(x,y, i):
            temp = board[x][y]
            board[x][y] = "#"
            if i == len(word):
                return True
            for dx, dy in directions:
                if 0 <= x + dx< len(board) and 0 <= y + dy < len(board[0]) and board[x + dx][y + dy] != "#" and board[x+dx][y + dy] == word[i]:
                    if dfs(x + dx, y + dy, i + 1):
                        return True
            board[x][y] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j, 1):
                        return True
        return False
