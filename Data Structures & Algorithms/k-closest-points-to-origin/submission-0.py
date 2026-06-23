class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, x, y))
        ans = []
        while len(ans) < k:
            dist, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans