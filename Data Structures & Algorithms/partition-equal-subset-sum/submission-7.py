class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total / 2
        #true if we can build a subset equal to half because that means the remaining also equals half. now the question becomes if we are able to make a sum of half without repeating any numberfs from nums
        #There are a few ways to do this that come to mind, backtracking of the different subset sums, dp top down, and dp bottom up
        #top down: can we make n - 1?
        #bottom up: builds the possible sums up from 0
        #either way we need to keep track of a used array because we cannot reuse
        possible =set()
        possible.add(0)
        def dfs(index, cur):
            if cur in possible:
                return True
            if index >= len(nums):
                return False
            if dfs(index + 1, cur - nums[index]) or dfs(index + 1, cur):
                possible.add(cur)
                return True
            return False
        return dfs(0, half)
            