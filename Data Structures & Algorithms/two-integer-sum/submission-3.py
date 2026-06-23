class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in map:
                return [map[needed], index]
            map[num] = index

        