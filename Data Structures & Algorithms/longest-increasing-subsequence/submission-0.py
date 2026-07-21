class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #create a dp array where dp[i] gives the longest subsequence
        #of the subarray starting at that index
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
