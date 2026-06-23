class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       seen = set()
       ret = []
       nums.sort()
       n = len(nums)
       for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = (nums[i], nums[j], nums[k])
                    if temp not in seen:
                        ret.append(list(temp))
                        seen.add(temp)
                elif nums[i] + nums[j] + nums[k] >0:
                    break
       return ret