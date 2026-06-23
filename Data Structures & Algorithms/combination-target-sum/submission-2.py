class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def backtrack(i):
            if sum(cur) == target:
                ans.append(cur.copy())
                return
            if i >= len(nums) or sum(cur) > target:
                return 
            #use nums[i]
            cur.append(nums[i])
            backtrack(i)
            #don't use nums[i]
            cur.pop()
            backtrack(i+1)
        backtrack(0)
        return ans
