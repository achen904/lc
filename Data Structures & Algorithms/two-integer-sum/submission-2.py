class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            needed = target - num
            map[needed] = index
        for index, num in enumerate(nums):
            if num in map and map[num] != index:
                if index < map[num]:
                    return [index, map[num]]
                else:
                    return [map[num], index]


        