class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        #key = sum, value = num ways ; sum : num_ways
        #without even iterating the array at all there is 1 way to make 0
        dp[0] = 1

        #iterate through nums and update possible sums we have seen after
        #that number ex: [1, 2]
            #first iteration dp[-1] = 1, dp[1] = 1
            #second iteration dp[-3] = 1, dp[-1] = 1, dp[3] = 1, dp[1] = 1
        
        for num in nums:
            new_dp = defaultdict(int)
            for cursum, count in dp.items():
                new_dp[cursum + num] += count #there are counts ways now to get cursum + num since before there were num ways to get cursum
                new_dp[cursum - num] += count
            dp = new_dp
        
        return dp[target]