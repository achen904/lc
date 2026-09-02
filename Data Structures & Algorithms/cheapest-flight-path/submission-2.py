class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):
            temp = dist.copy()
            for start, end, cost in flights:
                if dist[start] != float('inf') and dist[start] + cost < temp[end]:
                    temp[end] = dist[start] + cost
            dist = temp
        if dist[dst] != float('inf'):
            return dist[dst]
        return -1