class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        ans = 0
        while l < r:
            ans = max(ans, (r - l) * min(heights[r], heights[l]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -=1
            else:
                l += 1
        return ans