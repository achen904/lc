class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        cur = []

        def backtrack(i, val):
            if val == target:
                ans.append(cur.copy())
                return
            if i == len(candidates):
                return
            if candidates[i] + val <= target:
                cur.append(candidates[i])
                backtrack(i + 1, candidates[i] + val)
                cur.pop()
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                backtrack(i + 1, val)
            else:
                backtrack(i + 1, val)
        backtrack(0, 0)
        return ans