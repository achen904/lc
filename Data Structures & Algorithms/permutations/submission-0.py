class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        def backtrack(chosen):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for i in range(len(nums)):
                if not chosen[i]:
                    cur.append(nums[i])
                    chosen[i] = True
                    backtrack(chosen)
                    cur.pop()
                    chosen[i] = False
        chosen = [False] * len(nums)
        backtrack(chosen)
        return ans
            