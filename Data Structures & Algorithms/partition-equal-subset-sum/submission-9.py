class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #bottom up apporach
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total / 2
        seen = set()
        seen.add(0)
        for num in nums:
            temp = list(seen)
            for val in temp:
                if val + num <= half:
                    seen.add(val + num)
                if val + num == half:
                    return True
        return False