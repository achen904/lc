class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        def backtrack(i):
            if i == len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            backtrack(i + 1)
        backtrack(0)
        return ans