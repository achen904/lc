class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #[-4, -1, -1, 0, 1, 2]
        #[-1, -1, 1, 0]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                need = -nums[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == need:
                        ans.append([nums[i],nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > need:
                        r -= 1
                    else:
                        l += 1
                    while l > i + 1 and nums[l] == nums[l -1] and l < r:
                        l += 1
                    while r < len(nums) - 1 and nums[r] == nums[r + 1] and r > l:
                        r -= 1
                    
        return ans

