class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        neighbors = defaultdict(int)
        ans = 0
        for num in nums:
            if not neighbors[num]:
                left = neighbors[num - 1]
                right = neighbors[num + 1]
                total = 1 + neighbors[num - 1] + neighbors[num + 1]
                ans = max(ans, total)
                neighbors[num] = total
                neighbors[num - left] = total
                neighbors[num + right] = total
        return ans