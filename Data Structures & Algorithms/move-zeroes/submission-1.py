class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            #if r is not 0 then we swap it with l then increment l to know which index
            #we will be swapping with r next
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1