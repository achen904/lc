class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        connections = defaultdict(list)
        tickets.sort(reverse=True)
        for a, b in tickets:
            connections[a].append(b)
        
        ans = []
        
        def dfs(airport):
            while connections[airport]:
                dfs(connections[airport].pop())
            ans.append(airport)
        dfs("JFK")
        ans.reverse()
        return ans