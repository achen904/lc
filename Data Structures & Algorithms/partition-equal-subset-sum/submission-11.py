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
            temp = set()
            for val in seen:
                if val + num <= half:
                    temp.add(val + num)
                temp.add(val)
                if val + num == half:
                    return True
            seen = temp
        return False