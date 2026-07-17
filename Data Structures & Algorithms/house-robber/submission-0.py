class Solution:
    def rob(self, nums: List[int]) -> int:
        #another space optimized DP problem
        #At a given house i, the max amount of money we can have
        #is max(max(house i - 1), max(house i - 2) + nums[i])
        #we return the max at the last house

        #base case - max money at first house is robbing it
        oneBack = nums[0]
        twoBack = 0
        for i in range(1, len(nums)):
            curMax = max(nums[i] + twoBack, oneBack)
            twoBack = oneBack
            oneBack = curMax
        return oneBack