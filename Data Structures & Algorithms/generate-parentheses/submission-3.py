class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans =[]
        cur = []

        def backtrack(open, closed):
            if open + closed == 2*n:
                ans.append("".join(cur.copy()))
                return
            if open < n:
                cur.append("(")
                backtrack(open + 1, closed)
                cur.pop()
            if closed < open:
                cur.append(")")
                backtrack(open, closed + 1)
                cur.pop()
        backtrack(0,0)
        return ans