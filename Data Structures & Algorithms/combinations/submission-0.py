class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []

        def backtrack(i):
            if i > n:
                if len(cur) == k:
                    ans.append(cur.copy())
                return
            cur.append(i)
            backtrack(i + 1)
            cur.pop()
            backtrack(i + 1)
        backtrack(1)
        return ans

            