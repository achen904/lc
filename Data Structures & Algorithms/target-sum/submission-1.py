class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
     #backtracking soln
        dp = defaultdict(int)
        def backtrack(i, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            dp[(i, curSum)] = backtrack(i + 1, curSum + nums[i]) + backtrack(i + 1, curSum - nums[i])
            #at each index at nums[i] to current sum or subtract it
            #then feed that value to the new backtrack until we reach the end
            #base case, we reach the end, if we reach the end with the series of backtrcks
            #and we get curSum = target we found 1 way
            #dp[(i, cursum)] gives the number of ways we can get target with starting at our cursum at index i
            return dp[(i, curSum)]
        return backtrack(0,0)