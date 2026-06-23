class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        unique = set(nums)
        for num in unique:
            if num - 1 not in unique:
                temp = num
                count = 1
                while temp + 1 in unique:
                    count += 1
                    temp += 1
                ans = max(ans, count)
        return ans