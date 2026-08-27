class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = 0
        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            ans = max(cur, ans)
        return ans