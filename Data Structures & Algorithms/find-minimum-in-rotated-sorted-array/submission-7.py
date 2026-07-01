class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r)//2
            #if left most index is less than right most, then
            #the left most is the answer
            if nums[l] < nums[r]:
                return min(nums[l], ans)
            ans = min(nums[m] ,ans)
            #if left most is not less than right most but
            #left most is less than middle, that means the 
            #smallest value is to the right of m
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return ans
                