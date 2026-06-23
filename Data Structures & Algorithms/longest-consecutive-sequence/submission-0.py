class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        most = 0
        for n in nums:
            cur = 0
            if n - 1 not in hset:
                cur += 1
                while n + 1 in hset:
                    cur += 1
                    n += 1
            most = max(most, cur)
        return most