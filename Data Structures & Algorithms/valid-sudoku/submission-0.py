from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                    if board[r][c] in columns[c]:
                        return False
                    else:
                        columns[c].add(board[r][c])
                    square = (r//3) * 3 + (c//3)
                    if board[r][c] in squares[square]:
                        return False
                    else:
                        squares[square].add(board[r][c])
        return True
        