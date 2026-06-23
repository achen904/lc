class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        nums.sort(key=lambda n: (counts[n], -n))
        return nums