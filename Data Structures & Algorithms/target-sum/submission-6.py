class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            newdp = defaultdict(int)
            for val, ocurs in dp.items():
                newdp[val + num] += ocurs
                newdp[val - num] += ocurs
            dp = newdp
        return dp[target]