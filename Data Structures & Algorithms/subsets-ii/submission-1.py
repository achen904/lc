class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        cur = []
        def backtrack(i):
            if i >= len(nums):
                ans.append(cur.copy())
                return
            #use nums[i]
            cur.append(nums[i])
            backtrack(i+1)
            #don't use nums[i], nums[i+c] cannont = nums[i]
            c = 1
            while i + c < len(nums) and nums[i] == nums[i + c]:
                c += 1
            cur.pop()
            backtrack(i+c)
        backtrack(0)
        return ans

