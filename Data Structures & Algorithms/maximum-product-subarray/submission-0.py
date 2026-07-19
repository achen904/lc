class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #max can be created from single value, product of positives, or 2 negatives
        #so we should capture a local min which would be caused by our first negative if there is a negative
        #then if we see another negative it will create a positive which can then become a positive

        curMin, curMax = 1, 1
        ans = nums[0]

        for num in nums:
            temp = curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(temp * num, curMin * num, num)
            ans = max(ans, curMax)
        return ans