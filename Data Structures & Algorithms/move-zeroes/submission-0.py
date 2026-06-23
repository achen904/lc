class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while r < len(nums):
            while r < len(nums) and nums[r] == 0:
                r += 1
            while l < r and nums[l] != 0:
                l += 1
            if r < len(nums):
                nums[l], nums[r] = nums[r], nums[l]
            r += 1
            l += 1
        