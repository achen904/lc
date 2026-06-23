class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []

        def backtrack(closed, opened):
            if len(cur) == 2*n:
                ans.append("".join(cur.copy()))
                return
            if opened == closed:
                cur.append("(")
                backtrack(closed, opened + 1)
                cur.pop()
            elif opened == n:
                cur.append(")")
                backtrack(closed + 1, opened)
                cur.pop()
            elif opened > closed:
                cur.append(")")
                backtrack(closed + 1, opened)
                cur.pop()
                cur.append("(")
                backtrack(closed, opened + 1)
                cur.pop()
        backtrack(0, 0)
        return ans
            


            