class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        sub = []
        nums.sort()
        def backtrack(i, cur):
            if cur == target:
                ans.append(sub.copy())
                return
            if i >= len(nums) or cur + nums[i] > target:
                return
            sub.append(nums[i])
            cur += nums[i]
            backtrack(i, cur)
            sub.pop()
            cur -= nums[i]
            backtrack(i + 1, cur)
        backtrack(0, 0)
        return ans