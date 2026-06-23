from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        for num in nums:
            if num in map:
                map[num] = map[num] + 1
            else:
                map[num] = 1
        heap = []
        for num in map.keys():
            tup = (-map[num],num)
            heap.append(tup)
        heapq.heapify(heap)
        ret = []
        for i in range(k):
            tup = heapq.heappop(heap)
            ret.append(tup[1])
        return ret
        

        