class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #at every number we can either choose to use it or not
        #should keep track of a current sum so we don't have to call sum on cur
        #can only use if candidates[i] + cur <= target
        #base case is if cur == target or reached end
        ans = []
        cur = []
        candidates.sort()
        def backtrack(val, i):
            if val == target:
                ans.append(cur.copy())
                return
            if i == len(candidates):
                return
            if val + candidates[i] <= target:
                cur.append(candidates[i])
                backtrack(val + candidates[i], i + 1)
                cur.pop()
                while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                    i += 1
                backtrack(val, i + 1)
            else:
                backtrack(val, i + 1)
        backtrack(0, 0)
        return ans