class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = nums[0], 0

        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            ans = max(ans, cur)
        return ans
