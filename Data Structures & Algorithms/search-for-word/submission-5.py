class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()
        def valid(x,y):
            if not 0 <= x < len(board):
                return False
            if not 0 <= y < len(board[0]):
                return False
            return True
        def backtrack(i, j, index):
            nonlocal ans
            if index >= len(word) or word[index] != board[i][j]:
                return
            elif index == len(word) - 1:
                ans = True
            for dx,dy in directions:
                if valid(i + dx, j + dy) and (i + dx, j + dy) not in seen:
                    seen.add((i, j))
                    backtrack(i + dx, j + dy, index + 1)
                    seen.remove((i, j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    backtrack(i, j, 0)
        return ans
            

