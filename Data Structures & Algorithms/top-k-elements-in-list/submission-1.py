class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] = freqs[num] + 1
        buckets = defaultdict(list)
        for numbers in freqs:
            buckets[freqs[numbers]].append(numbers)
        ret = []
        for i in range (len(nums), 0, -1):
            if i in buckets:
                for num in buckets[i]:
                    ret.append(num)
            if len(ret) == k:
                return ret