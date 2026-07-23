class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #if we find a subset that sums to t then we return true
        #since total is even that means if we find a subset that is
        #half of it then the remaining subset has the same sum

        total = sum(nums)
        half = total // 2
        if total % 2 == 1:
            return False

        dp = [[False for _ in range(half + 1)] for _ in range(len(nums) + 1)]
        #dp[i][j] tells us True or False depending on if we can make a sum of j
        #using the elements up to and including i

        #base case, we can make a sum of 0 with any subset 
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, half + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                    #we can make j using a subset up to i by adding it to a previous
                    #subset that sums to be smaller than j or by using a previous
                    #subset that sums to j and we don't include nums[i - 1]
                else:
                    #if nums[i - 1] is bigger than J then we cannot include in the subset to be summed
                    #so the only way to reach J is if there is a previous subset that doesn't include
                    #nums[i - 1]
                    dp[i - 1][j]
        return dp[len(nums)][half]



        