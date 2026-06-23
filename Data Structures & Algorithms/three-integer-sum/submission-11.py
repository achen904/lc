class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i -1]:
               need = -nums[i]
               l, r = i + 1, len(nums) - 1
               while l < r:
                if nums[l] + nums[r] == need:
                    ans.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] > need:
                    r -= 1
                else:
                    l += 1
                while l > i and l > i + 1 and l < r and nums[l - 1] == nums[l]:
                    l += 1
                while r < len(nums) - 1 and l < r and nums[r + 1] == nums[r]:
                    r -= 1
        return ans


