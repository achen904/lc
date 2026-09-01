class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #bottom up
        dp = [1] * (len(nums)) #dp[i] gives the longest increasing subsequence using numbers up to i. all can be set to 1 because we only use that value
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)