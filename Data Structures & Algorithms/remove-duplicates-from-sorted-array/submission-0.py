class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #since the array is sorted in nondecreasing order
        #if the current element is different from the element behind
        #it then it is unique, so we if mainain a pointer that writes
        #to the index where we place the next unique element
        #and a pointer that finds the unique element
        #we can do this in O(n) and O(1) space
        #we can start at index 1, because we know that index 0 is unique
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l