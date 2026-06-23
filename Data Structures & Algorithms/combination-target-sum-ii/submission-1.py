class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        candidates.sort()

        def backtrack(i):
            total = sum(cur)
            if total == target:
                ans.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            #use i
            cur.append(candidates[i])
            backtrack(i + 1)
            #don't use i
            cur.pop()
            c = 1
            while i + c < len(candidates) and candidates[i] == candidates[i+c]:
                c += 1
            if i +c < len(candidates): 
                backtrack(i+c)
        backtrack(0)
        return ans