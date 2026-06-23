class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                #reached the end of our decision tree, add result
                ans.append(subset.copy())
                return
            #option1: use the value at i 
            subset.append(nums[i])
            dfs(i + 1)
            #option2: don't use the value at i
            subset.pop()
            dfs(i+1)
        dfs(0)
        return ans