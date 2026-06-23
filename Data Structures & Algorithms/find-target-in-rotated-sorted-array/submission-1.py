class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) //2
            if nums[m] == target:
                return m
            #m can be either contained in the sorted or unsorted side
            elif nums[l] <= nums[m]:
                #left is sorted side, so smallest value is nums[l] and largest
                #is nums[m], so if target isn't between
                #them, then it is on the unsorted side
                #if it is between them it is on this side
                if target < nums[l] or target > nums[m]: 
                    l = m + 1
                else:
                    r = m -1
            else:
                #right is sorted side so smallest value is nums[m] and 
                #largest value is nums[r]
                #if target is not between them then it is in the unsorted
                #side or not in the array at all
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
                
