class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []

        def backtrack(closed, opened):
            if len(cur) == 2*n:
                ans.append("".join(cur.copy()))
                return
            if opened < n:
                cur.append("(")
                backtrack(closed, opened + 1)
                cur.pop()
            if closed < opened:
                cur.append(")")
                backtrack(closed + 1, opened)
                cur.pop()
        backtrack(0, 0)
        return ans
            


            