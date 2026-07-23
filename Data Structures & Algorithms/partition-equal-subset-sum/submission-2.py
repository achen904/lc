class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2

        if total % 2 == 1:
            return False

        dp = [False] * (half + 1)

        dp[0] = True

        for num in nums:
            for j in range(half, num -1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[half]