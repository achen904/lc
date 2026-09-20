class Solution:
    def jump(self, nums: List[int]) -> int:
        #take the full jump or look ahead and see if there is a value in between cur and cur + nums[i] that will be better
        l, r = 0, 0
        ans = 0
        while r < len(nums) - 1:
            most = 0
            for i in range(l, r + 1):
                if i + nums[i] > most:
                    most = i + nums[i]
            l = r + 1
            r = most
            ans += 1
        return ans
