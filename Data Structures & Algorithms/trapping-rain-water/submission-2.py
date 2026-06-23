class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                if maxl - height[l] > 0:
                    ans += maxl-height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                if maxr - height[r] > 0:
                    ans += (maxr - height[r])
        return ans
            
            
            