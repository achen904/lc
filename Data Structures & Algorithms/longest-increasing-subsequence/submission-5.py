class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Every num by itself gives subsequence of 1
        #we can use top down dp by asking what is the longest common subsequence after me, if i am smaller than the number after me then add one to that subsequence
        memo = [-1] * len(nums)
        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            memo[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    memo[i] = max(1 + dfs(j), memo[i])
            return memo[i]
        return max(dfs(i) for i in range(len(nums)))
