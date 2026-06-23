class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        pre[0] = suf[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]
        for i in range (len(nums) - 2, -1, -1):
            suf[i] = nums[i+1] * suf[i+1]
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = pre[i] * suf[i]
        return ret