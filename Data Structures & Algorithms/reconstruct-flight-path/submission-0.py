class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        connections = defaultdict(list)

        for a, b in tickets:
            connections[a].append(b)
        
        for key in connections:
            connections[key].sort(reverse=True)
        
        ans = []
        
        def dfs(airport):
            while connections[airport]:
                dfs(connections[airport].pop())
            ans.append(airport)
        dfs("JFK")
        ans.reverse()
        return ans
