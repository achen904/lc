class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #since the array is sorted then rotated, we know that
        #we are guaranteed to have a sorted half if we split the array
        #anywhere. We can then levarage the sorted portion information to
        #see if our target is in the sorted portion. if not then it must either
        #be in the unsorted portion or not in the array at all
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1