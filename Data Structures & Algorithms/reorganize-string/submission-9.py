class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = []
        for ch, val in counts.items():
            if val > math.ceil(len(s) /2):
                return ""
            heapq.heappush(maxHeap, (-val, ch))
        ans = ""
        while maxHeap:
            val, ch = heapq.heappop(maxHeap)
            if len(ans) == 0 or ch != ans[-1]:
                ans += ch
                if val < -1:
                    heapq.heappush(maxHeap, (val + 1, ch))
            else:
                val2, ch2 = heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (val, ch))
                ans += ch2
                if val2 < -1:
                    heapq.heappush(maxHeap, (val2 + 1, ch2))
        return ans