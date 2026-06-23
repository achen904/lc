class Solution:
    # want k closest points
    # so need minheap which returns the closest point in the heap when pop
    # creating heap takes about O(n log n) where n is len(points)
    # creating ans takes O(k log n) so total run time is O(n log n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt(x**2 + y**2)
            heap.append((dist, x, y))
        heapq.heapify(heap)
        ans = []
        while len(ans) < k:
            dist, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans