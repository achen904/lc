class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use dictionaries to keep track of which numbers
        #have already been in seen in each column, row, and square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num != ".":
                    if num in rows[r]:
                        return False
                    if num in cols[c]:
                        return False
                    #use the row to find which row the square is in
                    #the use the column to find out how many to shift to right
                    square = (r // 3) * 3 + (c//3)
                    if num in squares[square]:
                        return False
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[square].add(num)
        return True