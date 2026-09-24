class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        minHeap = []
        curX, curY = points[0]
        heapq.heappush(minHeap, (0, curX, curY))
        ans = 0
        while len(seen) != len(points):
            dist, curX, curY = heapq.heappop(minHeap)
            if (curX, curY) not in seen:
                seen.add((curX, curY))
                ans += dist
                for x, y in points:
                    if (x,y) not in seen:
                        dist = abs(x - curX) + abs(y - curY)
                        heapq.heappush(minHeap, (dist, x, y))
        return ans