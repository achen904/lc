class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sub = []
        candidates.sort()
        def backtrack(i, cur):
            if cur == target:
                ans.append(sub.copy())
                return
            if i >= len(candidates) or cur + candidates[i] > target:
                return 
            cur += candidates[i]
            sub.append(candidates[i])
            backtrack(i + 1, cur)
            cur -= candidates[i]
            sub.pop()
            while i + 1< len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur)
        backtrack(0, 0)
        return ans
        