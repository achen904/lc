class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #we want the next greater value in the lexiographical order
        #so we want to increase the least significant digit
        #we can from right to left to see if we have a value that
        #is less than our right digit so that when we replace it, 
        #we increase.
        
        #find first smaller value
        r = len(nums) - 1
        l = r - 1
        while l >= 0 and r >= 0 and nums[l] >= nums[r]:
            r -= 1
            l -= 1
        #l is the the smaller value now, and we scan from right to left
        #to find the first value that is bigger than it
        if l < 0:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[l]:
                    nums[i], nums[l] = nums[l], nums[i]
                    break
            nums[l+1:] = reversed(nums[l+1:])
                
