class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #since we have a constraint of max k stops then dijkstras will not work
        #we must use bellman fordes
        dist = [float('inf')] * n
        dist[src] = 0
        #regular bellman forde gives cheapest path in general but since we want to limit paths we set our limit to k + 1 (using k + 1) edges which is k stops, regularly we use V edges where V = n in this case as each node in a regular graph can have at most V edges
        for i in range(k + 1):
            tmp_dist = dist.copy()
            for a, b, price in flights:
                if dist[a] != float('inf') and dist[a] + price < tmp_dist[b]:
                    tmp_dist[b] = dist[a] + price
            dist = tmp_dist
        return dist[dst] if dist[dst] != float('inf') else -1