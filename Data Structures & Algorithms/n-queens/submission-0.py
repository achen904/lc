class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        ans = []
        cur = []
        def backtrack(row):
            if len(cur) == n:
                ans.append(cur.copy())
                return
            #pick a column
            for col in range(n):
                #make sure not in cols, posDiag, and negDiag
                if col not in cols:
                    if row - col not in negDiag:
                        if row + col not in posDiag:
                            placement = ""
                            for i in range(col):
                                placement += "."
                            placement += "Q"
                            for i in range(col + 1, n):
                                placement += "."
                            cur.append(placement)
                            cols.add(col)
                            negDiag.add(row-col)
                            posDiag.add(row + col)
                            backtrack(row + 1)
                            cols.remove(col)
                            negDiag.remove(row-col)
                            posDiag.remove(row + col)
                            cur.pop()
                            
        backtrack(0)
        return ans
