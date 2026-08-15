class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        def backtrack(cur, i):
            if (cur, i) in dp:
                return dp[(cur, i)]
            if i == len(nums):
                if cur == target:
                    return 1
                return 0
            dp[(cur, i)] = backtrack(cur - nums[i], i + 1) + backtrack(cur + nums[i], i + 1)
            return dp[(cur, i)]
        return backtrack(0,0)