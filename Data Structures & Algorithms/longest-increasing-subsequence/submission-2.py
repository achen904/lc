from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        
        for i in range(1, len(nums)):
            #ans increases if the current element is larger than the smallest
            #ceiling of the current subsequence up i with size ans and dp[-1]
            #is what holds that value, so we append to dp 

            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                ind = bisect_left(dp, nums[i])
                dp[ind] = nums[i]
        return len(dp)

        