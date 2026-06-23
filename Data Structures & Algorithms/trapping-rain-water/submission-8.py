class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        maxl, maxr = height[l], height[r]
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(height[l], maxl)
                ans += maxl - height[l]
            else:
                r -= 1
                maxr = max(height[r], maxr)
                ans += maxr - height[r]
        return ans        