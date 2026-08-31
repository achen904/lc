class Solution:
    def rob(self, nums: List[int]) -> int:
        #Can either rob the current house and use the max from the house[i-2] or use house[i-1] and skip this house
        #can use bottom up dp to determine the max at the last house, where dp[i] returns the most amount of money after making decisions from house 0 to house i
        dp = [0] * len(nums)
        dp[0] = nums[0] #most money at first house is robbing it
        if len(nums) > 1:
            dp[1] = max(nums[1], nums[0])
        else:
            return dp[0]
        for i in range(2, len(nums)):
            #either rob this house or skip it
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[len(nums) - 1]
