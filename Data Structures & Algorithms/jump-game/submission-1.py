class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp[i] = True if we can reach the end of the array if we start
        #at the position
        dp = [False for _ in range(len(nums))]
        dp[len(nums) - 1] = True #base case, we can reach the end of the array if we start at the end
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            for j in range(1, num + 1):
                if i + j >= len(nums):
                    dp[i] = True
                    break
                if i + j < len(nums) and dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]

