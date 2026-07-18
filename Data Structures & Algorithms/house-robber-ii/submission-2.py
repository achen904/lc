class Solution:
    def rob(self, nums: List[int]) -> int:
        #because the first house and the last house are adjacent
        #at most, we can only include one of them in the houses
        #that we rob or we can choose to not include either of them
        #to determine which one we include, if either
        #we run the bottom up space optimized DP original algo
        #on the first to n - 1 and also run it on second to n
        #return the max between the 2

        #0 to n -1
        prev1 = nums[0]
        twoBack = 0
        for i in range(1, len(nums) - 1):
            cur = max(prev1, twoBack + nums[i])
            twoBack = prev1
            prev1 = cur
        
        #1 to n
        if len(nums) > 1:
            prev2 = nums[1]
            twoBack = 0
            for i in range(2, len(nums)):
                cur = max(prev2, twoBack + nums[i])
                twoBack = prev2
                prev2 = cur
            
            return max(prev1, prev2)
        return prev1