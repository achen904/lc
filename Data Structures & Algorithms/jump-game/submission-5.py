class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy
        #if we can reach the end from a previous index
        #then our new goal is to reach that new index
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0