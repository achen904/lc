class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i, height in enumerate(heights):
            if not stack:
                stack.append((i,height))
            elif stack[-1][1] <= height:
                stack.append((i, height))
            else:
                pop_index, pop_height = 0, 0
                while stack and stack[-1][1] > height:
                    pop_index, pop_height = stack.pop()
                    ans = max(ans, pop_height*(i - pop_index))
                stack.append((pop_index, height))
        while stack:
            pop_index, pop_height = stack.pop()
            ans = max(ans, pop_height*(len(heights) - pop_index))
        return ans


