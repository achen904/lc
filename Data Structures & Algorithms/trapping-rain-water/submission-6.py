class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        ans = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                value = min(maxl, maxr) - height[l]
                if value > 0:
                    ans += value
            else:
                r -= 1
                maxr = max(maxr, height[r])
                value = min(maxl, maxr) - height[r]
                if value > 0:
                    ans += value
        return ans

