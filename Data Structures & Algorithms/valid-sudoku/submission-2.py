class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != ".":
                    if val in rows[i] or val in cols[j]:
                        return False
                    box = (i // 3) * 3 + (j // 3)
                    if val in boxes[box]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box].add(val)
        return True