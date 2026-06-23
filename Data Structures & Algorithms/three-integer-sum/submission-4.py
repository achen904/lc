from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counts = defaultdict(int)
        ret = []
        for num in nums:
            counts[num] += 1
        for i in range(len(nums)):
            counts[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                counts[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if counts[target] > 0:
                    ret.append([nums[i], nums[j], target])
            for j in range(i + 1, len(nums)):
                counts[nums[j]] += 1
        return ret
                

        