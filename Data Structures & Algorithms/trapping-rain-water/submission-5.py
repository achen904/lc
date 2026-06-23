#to get the water stored at each index, we take the min of the biggest
#element to the left of it and the biggest element to the right of it
#the subtract the height of the current index
#A naive approach would to do manually find this for each index
#which would take O(n^2)
#However, we can do this in O(n) by precomputing the max prefix and suffix
#array for each index then running through the heigh array one more time
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = [0] * len(height)
        #calcluate prefix
        for i in range(len(height)):
            if len(prefix) == 0:
                prefix.append(height[i])
            else:
                prefix.append(max(height[i], prefix[-1]))
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                suffix[i] = height[i]
            else:
                suffix[i] = max(height[i], suffix[i + 1])
        ans = 0
        for i in range(len(height)):
            ans += min(prefix[i], suffix[i]) - height[i]
        return ans
        
