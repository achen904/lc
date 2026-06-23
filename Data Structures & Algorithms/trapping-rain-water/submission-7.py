class Solution:
    def trap(self, height: List[int]) -> int:
        #amount of water at an index is the min(maxl, maxr) - height[i]
        #we can use 2 pointers to keep track of the maxl, maxr and we
        #will move the pointer that is causing the bottleneck and update
        #the value. In example 1, maxl < maxr at the start so maxl will always
        #be the bottleneck in how much water we can hold. So we update the left
        #pointer to see if there is a larger value to the right of it. when
        #we calculate the amount of water that we can hold at the new index
        #we don't worry about the maxr because we know that the left side was
        #smaller and therefore is the bottleneck. So if our new index is greater
        #than maxl then it is our new biggest l and we cannot add any water
        #if our maxl is less, then our previous wall is still the bottle neck

        l, r = 0, len(height) - 1
        maxl = height[l]
        maxr = height[r]
        ans = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                ans += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                ans += maxr - height[r]
        return ans

