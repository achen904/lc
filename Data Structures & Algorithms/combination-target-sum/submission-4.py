class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def backtrack(i, val):
            if val == target:
                ans.append(cur.copy())
                return
            if i >= len(nums) or val > target:
                return 
            #use nums[i]
            cur.append(nums[i])
            backtrack(i, val + nums[i])
            #don't use nums[i]
            cur.pop()
            backtrack(i+1, val)
        backtrack(0, 0)
        return ans