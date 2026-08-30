class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #use dijkstra's to find the minimum path to each node from k
        #return the largest path of the minimums
        dist = [float('inf')] * (n + 1) #+1 because of 1 based indexing
        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k)) #(dist, node)
        connections = defaultdict(list) #start : finish, time
        for a, b, time in times:
            connections[a].append((b, time))

        while pq:
            cur, node = heapq.heappop(pq)
            for connected, time in connections[node]:
                if cur + time < dist[connected]:
                    dist[connected] = cur + time
                    heapq.heappush(pq, (cur + time, connected))
        ans = max(dist[1:])
        if ans == float('inf'):
            return -1
        return ans