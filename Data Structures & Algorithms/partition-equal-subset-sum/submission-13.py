class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #regular bottom up approach
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        #we can create a 2d array size half by len(nums) where dp[i][j] evaluates to True or False whether we are able to evaluate to i using nums up to j. this can also be space optimized to a 1d array size half as we only need to keep track of the previous iteration
        dp = [False] * (half + 1)
        dp[0] = True
        for num in nums:
            for i in range(half, -1, -1):
                if dp[i] and i + num <= half:
                    dp[i + num] = True
                if dp[half]:
                    return True
        return False
        