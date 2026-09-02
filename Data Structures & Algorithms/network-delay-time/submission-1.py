class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = [[] for i in range(n + 1)]
        for a, b, cost in times:
            connections[a].append((b, cost))
        pq = []
        heapq.heappush(pq, (0, k))
        costs = [float('inf')] * (n + 1)
        costs[k] = 0
        while pq:
            cost, node = heapq.heappop(pq)
            for neighbor, cur in connections[node]:
                if cost + cur < costs[neighbor]:
                    costs[neighbor] = cost + cur
                    heapq.heappush(pq, (cost + cur,neighbor))
        if max(costs[1:]) == float('inf'):
            return -1
        return max(costs[1:])

            