class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qs = []
        for i, query in enumerate(queries):
            qs.append([query, i])
        qs.sort()

        minHeap = []
        intervals.sort()
        pos = 0
        ans = [-1] * len(queries)
        for query, index in qs:
            while pos < len(intervals) and intervals[pos][0] <= query:
                length = intervals[pos][1] - intervals[pos][0] + 1
                heapq.heappush(minHeap, (length, intervals[pos][1]))
                pos += 1
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            if minHeap:
                val = minHeap[0][0]
                ans[index] = val
        return ans

        