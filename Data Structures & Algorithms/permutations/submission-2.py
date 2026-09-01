class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        def backtrack(used):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    cur.append(nums[i])
                    used[i] = True
                    backtrack(used)
                    used[i] = False
                    cur.pop()
        used = [False] * len(nums)
        backtrack(used)
        return ans