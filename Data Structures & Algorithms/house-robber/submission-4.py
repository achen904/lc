class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursiev version with memoization
        memo = [-1] * len(nums) #index : max
        def dfs(ind):
            if ind >= len(nums):
                return 0
            if memo[ind] != -1:
                return memo[ind]
            memo[ind] = max(nums[ind] + dfs(ind + 2), dfs(ind + 1))
            return memo[ind]
        return dfs(0)