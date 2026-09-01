class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        nums.sort()

        def backtrack(used):
            if len(cur) == len(nums):
                ans.append(cur.copy())
            i = 0
            while i < len(nums):
                if used[i]:
                    i += 1
                elif i >= 1 and not used[i - 1] and nums[i - 1] == nums[i]:
                    i += 1
                else:
                    cur.append(nums[i])
                    used[i] = True
                    backtrack(used)
                    used[i] = False
                    cur.pop()
                    i += 1
        used = [False] * len(nums)
        backtrack(used)
        return ans
