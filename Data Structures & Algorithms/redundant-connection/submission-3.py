class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycle = set()
        visited = set()
        connections = defaultdict(list)
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        #Define a DFS where we return True if we detect a cycle and False else
        cycleStart = -1
        def dfs(node, parent):
            #we track parent here because undirected graph
            #and don't want to count seeing the parent as a cycle
            nonlocal cycleStart
            if node in visited:
                if cycleStart == -1:
                    cycleStart = node
                    cycle.add(node)
                return True
            visited.add(node)
            for neighbor in connections[node]:
                if neighbor != parent:
                    if dfs(neighbor, node):
                        if cycleStart != -1:
                            cycle.add(node)
                        if cycleStart == node:
                            cycleStart = -1
                        return True
            return False
        dfs(1, -1)
        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a,b]
                        
#Naive solution: For every new edge, we add it to our adjacency list
#Run a DFS to see if a cycle exists. Return the last edge where a cycle exists
#However, this takes E*(V + E) time where V is the number of verticies
#E is the number of edges. We can improve this to V + E if we just run DFS
#once when we have the entire adjacency list built out.
#A graph with n vertices and n edges is guaranteed to have 1 cycle
#If we track all the edges that are in that cycle, then we can
#traverse the edges list in reverse and return the first edge 
#where both of the vertices are in the cycle set

