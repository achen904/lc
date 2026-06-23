class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in all:
                count = 1
                cur = num
                while cur + 1 in all:
                    cur += 1
                    count += 1
                ans = max(ans, count)
        return ans