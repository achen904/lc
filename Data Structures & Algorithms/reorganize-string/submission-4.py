class Solution:
    def reorganizeString(self, s: str) -> str:
        mxHeap = []
        counts = Counter(s)
        for ch in counts:
            if counts[ch] > math.ceil(len(s)/2):
                return ""
            tup = (-counts[ch], ch)
            mxHeap.append(tup)
        heapq.heapify(mxHeap)
        ans = ""
        while mxHeap:
            count, ch = heapq.heappop(mxHeap)
            if len(ans) == 0 or ch != ans[len(ans) - 1]:
                ans += ch
                if count < -1:
                    heapq.heappush(mxHeap,(count + 1, ch))
            else:
                count2, ch2 = heapq.heappop(mxHeap)
                heapq.heappush(mxHeap,(count, ch))
                ans += ch2
                if count2 < -1:
                    heapq.heappush(mxHeap,(count2 + 1, ch2))
        return ans


